# Contributing to rich-rst

Thanks for helping improve `rich-rst`.

## Development Setup

1. Fork and clone the repository.
2. Create and activate a virtual environment.
3. Install the package in editable mode with test dependencies.

Example:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
python -m pip install pytest pytest-cov
```

## Running Tests

Run the full test suite:

```bash
python -m pytest
```

Run tests with coverage (similar to CI):

```bash
python -m pytest --cov=rich_rst --cov-report term --cov-report xml --junitxml=testresults.xml
coverage report
```

## Building Docs

Documentation is in `docs/source` and uses Sphinx.

```bash
python -m pip install -r docs/requirements.txt
make -C docs html
```

On Windows, use:

```bat
docs\\make.bat html
```

## Code and Test Expectations

- Keep changes focused and small when possible.
- Add or update tests in `tests/` for behavior changes.
- Update docs when API, CLI, or rendering behavior changes.
- Keep vendored code updates limited to `tools/vendor_docutils.py` workflow and document them in `VENDORED.md`.

## Pull Requests

Before opening a pull request:

1. Rebase on the latest `main`.
2. Run tests locally.
3. Update `CHANGELOG.md` when appropriate.
4. Describe what changed and why.

PRs should include:

- Clear summary of behavior changes.
- Links to related issues (if any).
- Screenshots or terminal output for rendering changes when useful.

## Reporting Bugs / Requesting Features

- Bug reports: <https://github.com/wasi-master/rich-rst/issues>
- Feature requests: <https://github.com/wasi-master/rich-rst/issues>

For security issues, follow the private process in `SECURITY.md`.
