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

- Add support for `.. figure::` directive via a dedicated `visit_figure` handler
- Add inline `[N]` footnote reference rendering via `visit_footnote_reference`
- Add title rendering for doctest blocks
- Add support for the `title_reference` role
- Add support for showing line numbers in code blocks
- Add improved heading and title rendering
- Add RST grid and simple table rendering via `visit_table`
- Add dedicated `docinfo` node handlers with bibliographic transforms
- Add `visit_topic` handler and `apply_transforms` for table-of-contents (TOC) rendering

### Bug Fixes

- Fix malformed HTML output
- Fix footnotes not being left-aligned
- Fix superscript variable name typo
- Fix `_register_sphinx_roles()` registering roles multiple times
- Fix admonition body losing inline markup (now uses recursive visitor rendering)
- Fix `visit_line_block` not preserving nested line-block indentation
- Fix block quote silently dropping all paragraphs after the first
- Fix table caption not rendering for `csv-table` and `list-table` directives
- Fix abbreviation and acronym roles not rendering correctly
- Fix Rich markup injection via `Text.from_markup` with user-supplied content
- Fix definition list misidentifying children when no classifier is present
- Fix bug in math block rendering
- Fix `visit_pending` crashing
- Fix image formatting issues
- Fix `visit_paragraph` re-entering `visit_system_message` and not stopping
- Fix bug in footer rendering (footer only retaining the last element)
- Fix raw HTML title rendering
- Fix `ClassNotFound` / `IndexError` in `visit_raw`
- Fix `IndexError` when subtitle is absent in `visit_sidebar`
- Fix `TypeError` when concatenating `Text` with `""` in `visit_option_list`
- Fix file handle leak in the CLI
- Fix `IndexError` when renderables list is empty in `visit_field`
- Fix `KeyError` on unknown message type inside `visit_system_message`
- Rewrite list rendering to support unlimited nesting and any child node types

### CLI

- Move Rich tracebacks to CLI only (no longer shown in library usage)
