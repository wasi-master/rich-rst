"""Tests for directives that read external files.

File access is off by default so that rendering untrusted markup cannot
disclose local files.  When enabled, ``include`` and ``literalinclude`` must
stay inside the source document's directory.
"""

import os
import sys

import pytest

from rich_rst import RestructuredText
from rich_rst.__main__ import main

CANARY = 'CANARY_SECRET_d41d8cd9'


@pytest.fixture
def layout(tmp_path):
    """A docs directory with a canary file outside of it."""
    docs = tmp_path / 'docs'
    docs.mkdir()
    outside = tmp_path / 'outside'
    outside.mkdir()
    secret = outside / 'secret.txt'
    secret.write_text(f'{CANARY}\n', encoding='utf-8')
    secret_csv = outside / 'secret.csv'
    secret_csv.write_text(f'a,b\n{CANARY},x\n', encoding='utf-8')
    return docs, secret, secret_csv


def _leaking_directives(secret, secret_csv):
    return {
        'raw file': f'.. raw:: text\n   :file: {secret}\n',
        'raw url': f'.. raw:: text\n   :url: {secret.as_uri()}\n',
        'literalinclude': f'.. literalinclude:: {secret}\n',
        'include': f'.. include:: {secret}\n',
        'csv-table file': f'.. csv-table:: t\n   :file: {secret_csv}\n',
        'csv-table url': f'.. csv-table:: t\n   :url: {secret_csv.as_uri()}\n',
    }


@pytest.mark.parametrize('sphinx_compat', [True, False])
@pytest.mark.parametrize(
    'directive',
    ['raw file', 'raw url', 'literalinclude', 'include', 'csv-table file', 'csv-table url'],
)
def test_file_access_disabled_by_default(layout, sphinx_compat, directive):
    docs, secret, secret_csv = layout
    markup = _leaking_directives(secret, secret_csv)[directive]
    for filename in ('<rst-document>', str(docs / 'doc.rst')):
        out = RestructuredText(
            markup, sphinx_compat=sphinx_compat, filename=filename
        ).render_to_string(width=120)
        assert CANARY not in out


def test_file_access_disabled_after_sphinx_compat_render(layout):
    # Sphinx directive registration is process-global, so a later render with
    # sphinx_compat=False still sees the Sphinx literalinclude directive.
    _, secret, _ = layout
    RestructuredText('text', sphinx_compat=True).render_to_string()
    out = RestructuredText(f'.. literalinclude:: {secret}\n', sphinx_compat=False).render_to_string(
        width=120
    )
    assert CANARY not in out


def test_cli_file_access_disabled_by_default(layout, monkeypatch, capsys):
    docs, secret, _ = layout
    document = docs / 'doc.rst'
    document.write_text(f'.. literalinclude:: {secret}\n\n.. raw:: text\n   :file: {secret}\n')
    monkeypatch.setattr(sys, 'argv', ['rich-rst', str(document)])
    assert main() == 0
    assert CANARY not in capsys.readouterr().out


@pytest.mark.parametrize('directive', ['literalinclude', 'include'])
@pytest.mark.parametrize('kind', ['absolute', 'parent', 'symlink'])
def test_allowed_file_access_is_confined_to_source_directory(layout, directive, kind):
    docs, secret, _ = layout
    if kind == 'absolute':
        target = str(secret)
    elif kind == 'parent':
        target = os.path.relpath(secret, docs)
    else:
        link = docs / 'link.txt'
        try:
            link.symlink_to(secret)
        except (OSError, NotImplementedError):
            pytest.skip('symlinks not supported')
        target = 'link.txt'

    out = RestructuredText(
        f'.. {directive}:: {target}\n',
        filename=str(docs / 'doc.rst'),
        allow_file_access=True,
    ).render_to_string(width=120)
    assert CANARY not in out
    assert f'Rejected {directive} path outside source directory' in out


def test_allowed_file_access_reads_files_inside_source_directory(layout):
    docs, _, _ = layout
    (docs / 'snippet.py').write_text('x = 42\n', encoding='utf-8')
    (docs / 'part.rst').write_text('Included paragraph.\n', encoding='utf-8')
    out = RestructuredText(
        '.. literalinclude:: snippet.py\n\n.. include:: part.rst\n',
        filename=str(docs / 'doc.rst'),
        allow_file_access=True,
    ).render_to_string(width=120)
    assert 'x = 42' in out
    assert 'Included paragraph.' in out


def test_allowed_file_access_in_memory_markup_uses_cwd(layout, monkeypatch):
    docs, secret, _ = layout
    (docs / 'snippet.py').write_text('x = 42\n', encoding='utf-8')
    monkeypatch.chdir(docs)
    out = RestructuredText(
        f'.. literalinclude:: snippet.py\n\n.. literalinclude:: {secret}\n',
        allow_file_access=True,
    ).render_to_string(width=120)
    assert 'x = 42' in out
    assert CANARY not in out


def test_cli_allow_file_access_flag(layout, monkeypatch, capsys):
    docs, _, _ = layout
    (docs / 'snippet.py').write_text('x = 42\n', encoding='utf-8')
    document = docs / 'doc.rst'
    document.write_text('.. literalinclude:: snippet.py\n')
    monkeypatch.setattr(sys, 'argv', ['rich-rst', '--allow-file-access', str(document)])
    assert main() == 0
    assert 'x = 42' in capsys.readouterr().out
