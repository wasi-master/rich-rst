### [0.1.0]

- Initial Release

### [0.2.0]

- Added a command line interface

## [0.2.1], [0.2.2]

- Small documentation fixes

## [0.2.3]

- Fixed a bug with images without alt not being shown


## [0.2.5]

- Add `code_theme` parameter support for code blocks

## [1.0.0]

- Add support for most of the elements possible

## [1.0.1]

- Add support for the rubric element
- Fix a but where the error message wasn't parsed properly and therefore the parser crashed
- Fix system messages showing up twice
- Fix math blocks not having new lines

## [1.1.0]

### New Features

- Add support for acronym
- Add support for attribution
- Add support for citations and citation references
- Add support for decoration
- Add support for footers
- Add support for headers
- Add support for footnotes
- Add support for more elements in definition lists and improve formatting
- Add subscript and superscript support for some letters and symbols
- Add support for pending
- Add support for raw

- Add custom default lexer support
- Add support for guessing the lexer
### CLI

- Add code theme argument
- Add support for html output

### Docs

- Add demos to the demos folder
- Specify that caption is not possible
- Specify that figures are not supported

### Bugs

- Fix a bug where newlines weren't replaced with spaces as they should be
- Also get lexer name from format for literal codeblocks

## [1.1.1]

- Fix default lexer not being used sometimes
- Improve formatting for html with raw tag
- Add hide-error option for the CLI

## [1.1.2]

- Admonitions are now shown inside panels
- Fields are now shown inside tables
- Default value for guess_lexer is now False

## [1.1.3]

### Bugs

- Change caution style from `white on red` to just `red`
- Fix line breaks for enumerated lists and bullet lists

### New Features

- Add a filename parameter to the `RestructuredText` class
- Add another alias `reST`

### CLI

- Add new parameter for setting custom html width for word wrapping
- Add custom html layout for custom selection color, max width and font
- System messages now use the file name instead of `<string>`

## [1.1.4]

- Fix text being truncated (https://github.com/wasi-master/rich-rst/issues/1)
- Doctest blocks now use the `pycon` lexer rather than the default `python` lexer since the `pycon` lexer is especially made for console sessions

## [1.1.5]

- Fix a debug print message showing up
- Fix paragraphs not having adequate separation
- Fix code blocks having too much separation

## [1.1.6]

- Fix a issue where if a document started with bare text (not headers) then it would crash

## [1.1.7]

- Fix entire text being showed as a inline codeblock when only the first text is
- Fix https://github.com/Textualize/rich-cli/issues/31

## [1.2.0]

- Add Hyperlink Support
- Add python 3.11 and 3.12 classifiers
- Add UTF-8 header
- Add rich as a dependency
- Refactor __main__.py
- Fix too many arguments to unpack when visiting block quote

## [1.3.0]

- Fix docutils/optparse deprecation warnings
- No trailing newline by
- Add initial unit testing infrastructure

## [1.3.1]

- Remove trailing empty Text() objects that get displayed as newlines.

## [1.3.2]

- Convert to pyproject.toml, use setuptools_scm to manage version.
- Add support for common sphinx roles.
[maintenance] update expected test vectors
- Update the test expectations for Docutils 0.22

## [2.0.0]

### New Features

- Add `show_line_numbers` parameter to `RestructuredText` and the CLI (`--show-line-numbers`); applies to all syntax-highlighted blocks (literal, doctest, raw)
- Add six-level heading hierarchy: level 1 uses a double-box panel, level 2 a rounded-box panel, levels 3–6 use progressively lighter text styles (bold+underline → bold → underline → italic)
- Add `visit_figure` handler for the `.. figure::` directive; renders image, caption and legend inside a panel, with correct link when `:target:` is given
- Add `visit_table` handler for RST grid and simple tables, including optional caption/title and proper header row support
- Add `visit_topic` handler, rendering topics (including auto-generated table of contents) as a bordered panel
- Add `visit_footnote_reference` to render inline `[N]` footnote markers inline with the surrounding text
- Add `visit_title_reference` (the backtick `title` role) rendered in italic
- Add dedicated `docinfo` bibliographic-field handlers: `author`, `authors`, `organization`, `address`, `contact`, `version`, `revision`, `status`, `date`, `copyright` — all rendered in the shared field table
- Apply `DocTitle` and `DocInfo` transforms so recognised metadata fields are promoted to typed `docinfo` nodes before rendering
- Add `_render_admonition_body` helper: all admonition types (note, warning, tip, hint, attention, caution, danger, error, important, generic) now render their body through a sub-visitor, preserving inline markup (bold, italic, code, links, etc.) instead of stripping it to plain text
- Rewrite `visit_bullet_list` and `visit_enumerated_list` as recursive `_render_bullet_list` / `_render_enumerated_list` methods, supporting unlimited nesting depth, correct per-level indentation and markers (•, ∘, ▪), and arbitrary child node types including literal blocks
- Add `visit_rubric` as a distinct handler with an italic-dim rounded-box panel (previously delegated to `visit_title`)
- Add `_make_image_text` helper; images wrapped in a `reference` node (e.g. inside a figure) correctly use the outer link URI
- Footer now renders all elements (not just the last one) via `Group(*visitor.footer)`

### Bug Fixes

- Fix `visit_paragraph` re-entering `visit_system_message` without stopping — now raises `SkipChildren` immediately
- Fix block quote silently dropping all paragraphs after the first — now iterates every paragraph child
- Fix `visit_line_block` not preserving nested indentation — now uses a recursive `_render_line_block` helper
- Fix admonition body losing all inline markup — all admonition visitors use sub-visitor rendering instead of `.astext().replace("\n", " ")`
- Fix `visit_system_message` raising `KeyError` for unrecognised message types (`SEVERE`, `DEBUG`, unknown) — changed `dict[key]` lookup to `.get(key, "bold red")`
- Fix `visit_field` raising `IndexError` when `renderables` is empty — added a truthiness guard before inspecting the last element
- Fix `visit_option_list` raising `TypeError` when concatenating `Text` with `""` — changed the fallback to `Text()`
- Fix `visit_sidebar` raising `IndexError` when subtitle is absent — now safely handles one-child or subtitle-less sidebar nodes
- Fix `visit_raw` raising `ClassNotFound` / `IndexError` — delegate lexer guessing to the shared `_guess_lexer_name` helper
- Fix `visit_math_block` calling non-existent `self.renderables.append_text()` in the else branch
- Fix `visit_pending` — handler was misspelled as `visit_pendings`
- Fix `visit_problematic` missing `raise SkipChildren()`, causing double-rendering
- Fix definition list using `Text.from_markup` with user-supplied classifier text, allowing Rich markup injection — replaced with `Text(term, style=...)`
- Fix superscript translation table referenced via the wrong attribute name (`supercript` → `superscript`)
- Fix `_register_sphinx_roles()` registering roles repeatedly on each render — guarded with a module-level `_sphinx_roles_registered` flag
- Fix abbreviation and acronym roles not appending explanation text correctly
- Fix `visit_footnote` and `visit_generated` output being centre-aligned — changed to left-aligned
- Fix footer only retaining the last element — all collected footer renderables are now wrapped in `Group`
- Fix image link resolution when `:target:` is set

### CLI

- Add `--show-line-numbers` flag to display line numbers in syntax-highlighted code blocks
- Fix malformed HTML output: moved `<html>` before `<head>`, and replaced `<code><pre>` with the correct `<pre><code>` nesting
- Fix file handle leak: the input file is now opened with a `with` statement
- Move Rich traceback installation to the CLI entry point only — importing the library no longer installs the global traceback handler
- Fix `--save-html` KeyError in `__main__.py` (f-string left bare CSS braces that broke Rich's internal `format()` call)

### Documentation

- Rewrite docs/source/index.rst — clean description, standard Installation / Quick start / CLI / Contributing sections
- Rewrite docs/source/documentation.rst — single autoclass, aliases table, full CLI options table
- Rewrite docs/source/demonstration.rst — cleaner structure, consolidated sources table
