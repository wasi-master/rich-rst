import docutils, os, sys, re
import docutils.core, docutils.frontend, docutils.io, docutils.nodes
import docutils.parsers.rst, docutils.utils, docutils.parsers.rst.roles
import docutils.parsers.rst.languages.en

docutils.core.publish_doctree('Hello *world*')
base = os.path.dirname(docutils.__file__)
dpath = os.path.join(base, 'parsers/rst/directives')


def rewrite_vendored_source(content):
    """Rewrite docutils imports/paths so vendored files are self-contained."""
    # 1) from docutils... import ...
    content = re.sub(
        r'\bfrom\s+docutils(?=[\s.])',
        'from rich_rst._vendor.docutils',
        content,
    )

    # 2) import docutils.<submodule>
    # First rewrite direct imports to the vendored module path.
    content = re.sub(
        r'^([ \t]*)import\s+docutils\.(\S+)([ \t]*)$',
      r'\1import rich_rst._vendor.docutils.\2\3',
        content,
        flags=re.MULTILINE,
    )

    # 2b) Ensure a local `docutils` symbol exists once before each contiguous
    # block of rewritten submodule imports (preserving local indentation).
    lines = content.splitlines(keepends=True)
    rewritten_lines = []
    import_line_re = re.compile(r'^([ \t]*)import\s+rich_rst\._vendor\.docutils\.')
    from_line_tpl = '{indent}from rich_rst._vendor import docutils\n'
    previous_block_indent = None
    for line in lines:
      match = import_line_re.match(line)
      if match:
        indent = match.group(1)
        needed_from = from_line_tpl.format(indent=indent)
        if previous_block_indent != indent and (not rewritten_lines or rewritten_lines[-1] != needed_from):
          rewritten_lines.append(needed_from)
        previous_block_indent = indent
      else:
        previous_block_indent = None
      rewritten_lines.append(line)
    content = ''.join(rewritten_lines)

    # 3) import docutils [as alias]
    content = re.sub(
        r'^([ \t]*)import\s+docutils(\s+as\s+\w+)?([ \t]*)$',
        r'\1from rich_rst._vendor import docutils\2\3',
        content,
        flags=re.MULTILINE,
    )

    # 4) Dynamic import strings and package-prefix constants used by Docutils.
    # Rewrite only when they appear inside string literals.
    literal_prefixes = (
        'docutils.writers.',
        'docutils.readers.',
        'docutils.parsers.',
        'docutils.languages.',
        'docutils.parsers.rst.languages.',
    )
    for prefix in literal_prefixes:
        content = re.sub(
            fr'(?<!rich_rst\._vendor\.)(?<=["\']){re.escape(prefix)}',
            f'rich_rst._vendor.{prefix}',
            content,
        )

    return content


def iter_python_files(base_dir, exclude_dirs=None):
    """Yield Python file paths under base_dir, excluding selected subdirectories."""
    exclude_dirs = exclude_dirs or set()
    for root, dirs, filenames in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
        for filename in filenames:
            if filename.endswith('.py'):
                yield os.path.join(root, filename)


def patch_project_imports(paths):
    """Rewrite docutils imports in project and tests to vendored imports."""
    patched = []
    for path in paths:
        if not os.path.isdir(path):
            continue
        for file_path in iter_python_files(path, exclude_dirs={'_vendor', '__pycache__'}):
            with open(file_path, encoding='utf-8') as f:
                original = f.read()

            rewritten = rewrite_vendored_source(original)
            if rewritten == original:
                continue

            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(rewritten)
            patched.append(file_path)

    return patched

# Collect all files
mods = sorted([m for m in sys.modules if m.startswith('docutils')])
files = set()
for modname in mods:
    mod = sys.modules[modname]
    path = getattr(mod, '__file__', None)
    if path and path.endswith('.py'):
        files.add(path)

for f in os.listdir(dpath):
    if f.endswith('.py') and f != '__init__.py':
        p = os.path.join(dpath, f)
        files.add(p)

files = sorted(files)

vendor_dir = './rich_rst/_vendor'
os.makedirs(vendor_dir, exist_ok=True)

for src_path in files:
    rel = os.path.relpath(src_path, os.path.dirname(base))  # relative to site-packages
    dst_path = os.path.join(vendor_dir, rel)
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)

    with open(src_path) as f:
        content = f.read()

    content = rewrite_vendored_source(content)

    with open(dst_path, 'w') as f:
        f.write(content)

print(f"Vendored {len(files)} files to {vendor_dir}")
print("Sample directory structure:")
for root, dirs, filenames in os.walk(vendor_dir):
    dirs.sort()
    level = root.replace(vendor_dir, '').count(os.sep)
    indent = '  ' * level
    print(f'{indent}{os.path.basename(root)}/')
    for filename in sorted(filenames):
        if filename != '__pycache__':
            print(f'{indent}  {filename}')

# Rewrite imports in local project files so vendoring requires no manual edits.
patched_project_files = patch_project_imports(['./rich_rst', './tests'])
print(f"Patched imports in {len(patched_project_files)} source/test files")
for file_path in patched_project_files:
    print(f"  {file_path}")

# Create VENDORED.md
vendored_md_content = """# Vendored Dependencies

This package vendors a subset of [Docutils](https://docutils.sourceforge.io/) rather than
declaring it as an install-time dependency. This document explains what was vendored, why,
and what the licensing implications are.

## Why vendoring?

Docutils is the only Python library capable of parsing reStructuredText into a document
tree that rich-rst can walk. It is mature, stable, and has no Python dependencies of its
own. However, because the Docutils distribution ships one Emacs Lisp file
(`tools/editors/emacs/rst.el`) under the GNU General Public License v3+, automated
license scanners flag the entire package as "GPL" — even though that file is never
installed by `pip` and has no relationship to the Python code. This created compliance
friction for enterprise users of libraries that depend on rich-rst (notably FastMCP via
cyclopts).

Vendoring the specific Python modules that rich-rst actually uses eliminates the
dependency entirely, removes any ambiguity for scanners, and keeps rich-rst a
zero-dependency package (aside from `rich` itself).

## What was vendored

**Source:** Docutils 0.22.4  
**Upstream URL:** https://docutils.sourceforge.io/  
**PyPI:** https://pypi.org/project/docutils/0.22.4/  
**Vendored into:** `rich_rst/_vendor/docutils/`

The following 41 Python modules were copied verbatim (aside from rewriting internal
`from docutils` / `import docutils` references to point at the vendored path
`rich_rst._vendor.docutils`):

| Module | License |
|---|---|
| `docutils/__init__.py` | Public Domain |
| `docutils/core.py` | Public Domain |
| `docutils/frontend.py` | Public Domain |
| `docutils/io.py` | Public Domain |
| `docutils/nodes.py` | Public Domain |
| `docutils/statemachine.py` | Public Domain |
| `docutils/languages/__init__.py` | Public Domain |
| `docutils/languages/en.py` | Public Domain |
| `docutils/parsers/__init__.py` | Public Domain |
| `docutils/parsers/rst/__init__.py` | Public Domain |
| `docutils/parsers/rst/roles.py` | Public Domain |
| `docutils/parsers/rst/states.py` | Public Domain |
| `docutils/parsers/rst/tableparser.py` | Public Domain |
| `docutils/parsers/rst/directives/__init__.py` | Public Domain |
| `docutils/parsers/rst/directives/admonitions.py` | Public Domain |
| `docutils/parsers/rst/directives/body.py` | Public Domain |
| `docutils/parsers/rst/directives/html.py` | Public Domain |
| `docutils/parsers/rst/directives/images.py` | Public Domain |
| `docutils/parsers/rst/directives/misc.py` | Public Domain |
| `docutils/parsers/rst/directives/parts.py` | Public Domain |
| `docutils/parsers/rst/directives/references.py` | Public Domain |
| `docutils/parsers/rst/directives/tables.py` | Public Domain |
| `docutils/parsers/rst/languages/__init__.py` | Public Domain |
| `docutils/parsers/rst/languages/en.py` | Public Domain |
| `docutils/readers/__init__.py` | Public Domain |
| `docutils/readers/doctree.py` | Public Domain |
| `docutils/readers/standalone.py` | Public Domain |
| `docutils/transforms/__init__.py` | Public Domain |
| `docutils/transforms/frontmatter.py` | Public Domain |
| `docutils/transforms/misc.py` | Public Domain |
| `docutils/transforms/references.py` | Public Domain |
| `docutils/transforms/universal.py` | Public Domain |
| `docutils/utils/__init__.py` | Public Domain |
| `docutils/utils/_roman_numerals.py` | Public Domain |
| `docutils/utils/_typing.py` | Public Domain |
| `docutils/utils/code_analyzer.py` | Public Domain |
| `docutils/utils/urischemes.py` | Public Domain |
| `docutils/utils/punctuation_chars.py` | BSD 2-Clause |
| `docutils/utils/smartquotes.py` | BSD 2-Clause (see note) |
| `docutils/writers/__init__.py` | Public Domain |
| `docutils/writers/null.py` | Public Domain |

**Note on `smartquotes.py`:** This file is a 2-Clause BSD-licensed adaptation by Günter
Milde (© 2010–2023) of SmartyPants (© 2003 John Gruber, 3-Clause BSD) and
smartypants.py (© 2004, 2007 Chad Miller, 2-Clause BSD). Full license text is in
`_vendor/LICENSES.txt`.

## What was NOT vendored

The following parts of Docutils are **not present** in this repository and are **not
used** by rich-rst at runtime:

- `tools/editors/emacs/rst.el` — the GPL v3+ Emacs Lisp file that triggers scanner
  alerts. Not a Python module; never imported.
- `docutils/utils/math/` — math rendering modules (BSD-licensed but unused by rich-rst).
- `docutils/writers/` — all output writers except `writers/null.py` (unused).
- `docutils/parsers/commonmark_wrapper.py` — CommonMark parser (unused).
- All test files, documentation, and build tools.

## Keeping the vendor copy up to date

When upgrading the vendored copy to a newer Docutils release:

1. Install the target version: `pip install docutils==X.Y.Z`
2. Run `python tools/vendor_docutils.py` (see `tools/` directory) to re-copy and
   rewrite imports.
3. Run the test suite to confirm nothing broke.
4. Update the version number in this file and in `_vendor/LICENSES.txt`.
5. Commit the updated `rich_rst/_vendor/docutils/` tree and both docs.

The internal import rewriting performed by the vendor script is the only modification
made to the upstream source. No logic is changed.
"""

vendored_md_path = './VENDORED.md'
if not os.path.exists(vendored_md_path):
    with open(vendored_md_path, 'w') as f:
        f.write(vendored_md_content)
    print(f"Created {vendored_md_path}")

# Create rich_rst/_vendor/License.txt
license_txt_content = """================================================================================
Licenses for vendored code in rich_rst/_vendor/
================================================================================

This directory contains a vendored subset of Docutils 0.22.4, copied here to
eliminate the docutils PyPI dependency and remove GPL code from the dependency
tree. See VENDORED.md for the full rationale.

All 41 vendored Python modules are either dedicated to the public domain or
released under the BSD 2-Clause License. No GPL-licensed file is included.

--------------------------------------------------------------------------------
PART 1 — Public Domain (39 of 41 files)
--------------------------------------------------------------------------------

The following files have been dedicated to the public domain by their authors.
They carry no license requirements and no restrictions on copying or usage.

  docutils/__init__.py
  docutils/core.py
  docutils/frontend.py
  docutils/io.py
  docutils/nodes.py
  docutils/statemachine.py
  docutils/languages/__init__.py
  docutils/languages/en.py
  docutils/parsers/__init__.py
  docutils/parsers/rst/__init__.py
  docutils/parsers/rst/directives/__init__.py
  docutils/parsers/rst/directives/admonitions.py
  docutils/parsers/rst/directives/body.py
  docutils/parsers/rst/directives/html.py
  docutils/parsers/rst/directives/images.py
  docutils/parsers/rst/directives/misc.py
  docutils/parsers/rst/directives/parts.py
  docutils/parsers/rst/directives/references.py
  docutils/parsers/rst/directives/tables.py
  docutils/parsers/rst/languages/__init__.py
  docutils/parsers/rst/languages/en.py
  docutils/parsers/rst/roles.py
  docutils/parsers/rst/states.py
  docutils/parsers/rst/tableparser.py
  docutils/readers/__init__.py
  docutils/readers/doctree.py
  docutils/readers/standalone.py
  docutils/transforms/__init__.py
  docutils/transforms/frontmatter.py
  docutils/transforms/misc.py
  docutils/transforms/references.py
  docutils/transforms/universal.py
  docutils/utils/__init__.py
  docutils/utils/_roman_numerals.py
  docutils/utils/_typing.py
  docutils/utils/code_analyzer.py
  docutils/utils/urischemes.py
  docutils/writers/__init__.py
  docutils/writers/null.py

Public Domain Dedication (from the Docutils project):

  The persons who have associated their work with this project (the
  "Dedicator": David Goodger and the many contributors to the Docutils
  project) hereby dedicate the entire copyright in the work of authorship
  known as "Docutils" to the public domain.

  Most of the files included in this project have been placed in the public
  domain, and therefore have no license requirements and no restrictions on
  copying or usage.

  Upstream project:  https://docutils.sourceforge.io/
  Upstream COPYING:  https://docutils.sourceforge.io/COPYING.html

--------------------------------------------------------------------------------
PART 2 — BSD 2-Clause License (2 of 41 files)
--------------------------------------------------------------------------------

The following files are released under the BSD 2-Clause License:

  docutils/utils/smartquotes.py
  docutils/utils/punctuation_chars.py

Both files were authored by Günter Milde. smartquotes.py is additionally
derived from SmartyPants (John Gruber, BSD 3-Clause) and smartypants.py
(Chad Miller, BSD 2-Clause); their licenses are reproduced below.

------  docutils/utils/punctuation_chars.py  ----------------------------------

  Copyright © 2011, 2017 Günter Milde.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:

  1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

  2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
  POSSIBILITY OF SUCH DAMAGE.

------  docutils/utils/smartquotes.py  ----------------------------------------

  Top-level file copyright:
  Copyright © 2010–2023 Günter Milde,
              original SmartyPants © 2003 John Gruber,
              smartypants.py © 2004, 2007 Chad Miller.

  The file is released as a whole under the BSD 2-Clause License (in short:
  copying and distribution, with or without modification, are permitted in
  any medium without royalty provided the copyright notices and this notice
  are preserved; the file is offered as-is, without any warranty).

  The file contains and derives from three separately-licensed components:

  -- SmartyPants (BSD 3-Clause) --

    Copyright (c) 2003 John Gruber (http://daringfireball.net/)
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are
    met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in
      the documentation and/or other materials provided with the
      distribution.

    * Neither the name "SmartyPants" nor the names of its contributors
      may be used to endorse or promote products derived from this
      software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

  -- smartypants.py (BSD 2-Clause) --

    smartypants.py is a derivative work of SmartyPants.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are
    met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in
      the documentation and/or other materials provided with the
      distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

  -- Günter Milde adaptations (BSD 2-Clause) --

    Copyright © 2010–2023 Günter Milde.

    Released under the terms of the 2-Clause BSD license:
    https://opensource.org/licenses/BSD-2-Clause

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are
    met:

    1. Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in
       the documentation and/or other materials provided with the
       distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

--------------------------------------------------------------------------------
What is NOT vendored
--------------------------------------------------------------------------------

The following file exists in the Docutils source tree but is NOT vendored here
and is NOT distributed with any Docutils wheel or sdist Python installation:

  tools/editors/emacs/rst.el  —  GPL v3 or later (Emacs editor support file)

This Emacs Lisp file is the sole reason Docutils' PyPI metadata lists GPL as
one of its licenses. It is never imported by Python code, was not present in
the installed wheel, and is entirely absent from this vendored copy.

================================================================================
"""

license_txt_path = os.path.join(vendor_dir, 'License.txt')
if not os.path.exists(license_txt_path):
    with open(license_txt_path, 'w') as f:
        f.write(license_txt_content)
    print(f"Created {license_txt_path}")