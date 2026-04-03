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

### Highlights

- Vendored `docutils` into `rich_rst` and removed it as an external dependency (licensing and packaging simplification).
- Added `show_errors` (replacing `hide_errors`) and `show_line_numbers` in both API and CLI.
- Added a `--version` flag to the cli
- Expanded core rendering support for major RST structures: tables, figures, topics, rubric, footnote references, title references, and richer `docinfo` metadata handling.
- Improved heading styling with a clear six-level visual hierarchy.
- Improved code and math rendering: clearer literal block language labels and math blocks rendered in a dedicated panel.

### Sphinx Compatibility

- Added support for key Sphinx directives under `sphinx_compat=True`, including version/deprecation blocks, code directives, document-structure directives (`toctree`, `glossary`, `hlist`, `only`, etc.), and domain object directives (Python/C/C++/JS).
- Added broad Sphinx role coverage, including `:pep:`, `:rfc:`, cross-reference roles, and improved handling for roles such as `:command:`, `:program:`, `:dfn:`, `:menuselection:`, `:samp:`, and `:file:`.
- Added silent no-op handling for directives such as `index`, `tabularcolumns`, `currentmodule`, and `auto*` autodoc directives to avoid noisy parsing errors.

### Stability and Rendering Fixes

- Fixed multiple visitor edge cases and crashes (system messages, pending/problematic nodes, sidebar subtitle handling, option/field guards, raw lexer resolution, and paragraph recursion behavior).
- Fixed list rendering comprehensively: nested bullet/enumerated lists, custom numbering styles, proper indentation, and preserved inline markup.
- Fixed block and quote rendering issues, including dropped paragraphs, line-block indentation, and quote spacing.
- Fixed footnote/generated alignment and footer rendering so all collected footer elements are preserved.
- Fixed markup safety issue in definition-list classifier rendering (avoids unintended Rich markup interpretation).
- Fixed image target-link resolution in figure/reference contexts.

### CLI

- Added `--show-line-numbers` support for syntax-highlighted code blocks.
- Fixed HTML output structure (`<html>/<head>` order and `<pre><code>` nesting).
- Fixed file-handle leak when reading input files.
- Moved Rich traceback installation to CLI entry only (importing library no longer changes global traceback behavior).
- Fixed `--save-html` format-string `KeyError` caused by bare CSS braces.

### Documentation and Tests

- Rewrote key docs pages (`index.rst`, `documentation.rst`, `demonstration.rst`) for clearer onboarding and reference flow.
- Reworked tests to improve granular coverage of individual features.