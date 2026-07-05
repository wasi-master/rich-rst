# Copilot instructions for rich-rst

Purpose
- Short guidance to help Copilot sessions understand build/test commands, the high-level architecture, and repository-specific conventions.

Build / Install
- Install for development (recommended):
  python -m venv .venv
  source .venv/bin/activate
  python -m pip install -U pip
  python -m pip install -e ".[tests]"

- Install latest released package:
  pip install rich-rst

Tests
- Full test suite:
  python -m pytest

- CI-like (coverage + xml + junit):
  python -m pytest --cov=rich_rst --cov-report term --cov-report xml --junitxml=testresults.xml
  coverage report

- Run a single test file:
  python -m pytest tests/test_api.py

- Run a single test function or node id:
  python -m pytest tests/test_api.py::test_specific_function
  # or search by keyword
  python -m pytest -k "keyword"

Docs
- Build docs (Sphinx):
  python -m pip install -r docs/requirements.txt
  make -C docs html
  # On Windows: docs\make.bat html

Packaging
- Project uses setuptools via pyproject.toml. The package is built/installed in editable mode for dev workflows (see above).

Continuous integration
- CI workflow: .github/workflows/tests.yaml runs matrix across OSes and Python 3.9–3.14 and installs with `pip install -e .` and pytest/coverage.

High-level architecture (big picture)
- Package: rich_rst/ — main Python package exposing RestructuredText and CLI (python -m rich_rst).
- CLI entrypoint: rich_rst.__main__.py (parses args, renders to console or exports HTML).
- Vendored dependency: rich_rst/_vendor/docutils/ — a trimmed copy of Docutils used at runtime (see VENDORED.md).
- Documentation: docs/ (Sphinx sources and Makefile).
- Tests: tests/ (pytest-based unit tests and conftest.py).
- Tools: tools/ contains helper scripts (e.g., tools/vendor_docutils.py used to refresh vendored docutils).

Key repository conventions (not obvious from a single file)
- Vendoring: Docutils is intentionally vendored. Updates must follow VENDORED.md exactly: pip install target docutils version, run tools/vendor_docutils.py, run tests, update VENDORED.md and license headers.
- Tests extras: `.[tests]` extra in pyproject.toml installs pytest and pytest-cov. Use that for consistent dev installs.
- Coverage and CI artifacts: tests produce coverage xml and junit xml (testresults.xml) for CI integrations.
- Supported Python versions: declared in pyproject.toml: 3.8–3.14. CI matrix exercises 3.9–3.14.
- Do not modify files under rich_rst/_vendor/docutils/ manually outside the vendor script; treat them as an upstream copy.

Notes for Copilot sessions
- Prefer suggestions that respect the vendored docutils approach (use tools/vendor_docutils.py to refresh upstream code).
- Use the CLI and tests for quick verification: `python -m rich_rst file.rst` and `python -m pytest tests/test_...py::test_name`.
- There is no project-wide linter configuration checked in; suggest adding one if linting guidance is needed.

Other AI assistant configs
- None of the known assistant config files (CLAUDE.md, AGENTS.md, .cursorrules, .windsurfrules, etc.) are present.

Questions
- Configure MCP servers? If you'd like, specify which tooling (e.g., Playwright for web docs) and it can be added.

--
Generated summary: added .github/copilot-instructions.md to explain build/test commands, architecture, and repo-specific conventions for future Copilot sessions.
