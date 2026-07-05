"""Tests for the rich-rst CLI entrypoint."""

import os
import sys
import tempfile

import pytest

from rich_rst.__main__ import main


@pytest.mark.parametrize(
    'error_type,error_message',
    [
        (FileNotFoundError, 'missing.rst'),
        (PermissionError, 'unreadable.rst'),
    ],
)
def test_cli_reports_file_read_errors(monkeypatch, capsys, error_type, error_message):
    path = error_message

    def fake_open(*args, **kwargs):
        raise error_type(path)

    monkeypatch.setattr(sys, 'argv', ['rich-rst', path])
    monkeypatch.setattr('builtins.open', fake_open)

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 1
    assert 'File Error' in captured.out
    assert f'Path: {path!r}' in captured.out
    assert 'Check that the file exists' in captured.out
    assert 'Traceback' not in captured.out


# ── --list-html-themes ────────────────────────────────────────────────────────


def test_list_html_themes_exits_zero(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['rich-rst', '--list-html-themes'])
    exit_code = main()
    assert exit_code == 0


def test_list_html_themes_prints_theme_names(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', ['rich-rst', '--list-html-themes'])
    main()
    captured = capsys.readouterr()
    lines = [line.strip() for line in captured.out.splitlines() if line.strip()]
    assert 'dracula' in lines
    assert 'monokai' in lines
    assert 'default' in lines


def test_list_html_themes_does_not_require_path(monkeypatch, capsys):
    """--list-html-themes must not fail even without a PATH argument."""
    monkeypatch.setattr(sys, 'argv', ['rich-rst', '--list-html-themes'])
    exit_code = main()
    assert exit_code == 0


# ── --html-theme ──────────────────────────────────────────────────────────────


def test_html_theme_argument_accepted(monkeypatch, tmp_path):
    """--html-theme monokai must be accepted without error."""
    rst_file = tmp_path / 'test.rst'
    rst_file.write_text('Hello world.', encoding='utf-8')
    html_out = tmp_path / 'out.html'
    monkeypatch.setattr(
        sys,
        'argv',
        ['rich-rst', str(rst_file), '--html-theme', 'monokai', '--save-html', str(html_out)],
    )
    exit_code = main()
    assert exit_code == 0
    assert html_out.exists()


# ── --output / -o ─────────────────────────────────────────────────────────────


def test_output_flag_writes_to_file(monkeypatch, tmp_path):
    rst_file = tmp_path / 'test.rst'
    rst_file.write_text('Hello **world**.', encoding='utf-8')
    out_file = tmp_path / 'rendered.txt'
    monkeypatch.setattr(
        sys,
        'argv',
        ['rich-rst', str(rst_file), '-o', str(out_file)],
    )
    exit_code = main()
    assert exit_code == 0
    assert out_file.exists()
    content = out_file.read_text(encoding='utf-8')
    assert 'Hello' in content
    assert 'world' in content


def test_output_short_flag(monkeypatch, tmp_path):
    rst_file = tmp_path / 'test.rst'
    rst_file.write_text('Short text.', encoding='utf-8')
    out_file = tmp_path / 'out.txt'
    monkeypatch.setattr(
        sys,
        'argv',
        ['rich-rst', str(rst_file), '-o', str(out_file)],
    )
    exit_code = main()
    assert exit_code == 0
    content = out_file.read_text(encoding='utf-8')
    assert 'Short text.' in content


def test_output_flag_error_on_bad_path(monkeypatch, capsys):
    import builtins

    real_open = builtins.open

    def selective_open(path, *args, **kwargs):
        # fail only for the output file write (mode 'w')
        mode = args[0] if args else kwargs.get('mode', 'r')
        if mode == 'w':
            raise OSError('no space left')
        return real_open(path, *args, **kwargs)

    with tempfile.TemporaryDirectory() as tmpdir:
        rst_path = os.path.join(tmpdir, 'test.rst')
        with open(rst_path, 'w') as f:
            f.write('Hello world.')

        monkeypatch.setattr(sys, 'argv', ['rich-rst', rst_path, '-o', '/bad/path/out.txt'])
        monkeypatch.setattr('builtins.open', selective_open)

        exit_code = main()
        assert exit_code == 1


# ── New CLI coverage tests ───────────────────────────────────────────────────


def test_cli_missing_path_raises_system_exit(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['rich-rst'])
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2


def test_cli_debug_mode_enables_logging(monkeypatch, tmp_path):
    rst_file = tmp_path / 'test.rst'
    rst_file.write_text('Hello world.', encoding='utf-8')
    monkeypatch.setattr(sys, 'argv', ['rich-rst', str(rst_file), '--debug'])

    # We can also mock basicConfig or logging to ensure no actual global side effects,
    # but running it verifies the logging block executes.
    import logging
    original_basic_config = logging.basicConfig
    called = []

    def mock_basic_config(*args, **kwargs):
        called.append(kwargs)
        original_basic_config(*args, **kwargs)

    monkeypatch.setattr(logging, 'basicConfig', mock_basic_config)
    exit_code = main()
    assert exit_code == 0
    assert any(c.get('level') == logging.DEBUG for c in called)


def test_cli_stdin_reading(monkeypatch, capsys):
    import io
    fake_stdin = io.StringIO('Stdin *content*.')
    monkeypatch.setattr(sys, 'stdin', fake_stdin)
    monkeypatch.setattr(sys, 'argv', ['rich-rst', '-'])

    exit_code = main()
    assert exit_code == 0
    captured = capsys.readouterr()
    assert 'Stdin' in captured.out
    assert 'content' in captured.out


def test_cli_parse_error_handling(monkeypatch, capsys, tmp_path):
    rst_file = tmp_path / 'test.rst'
    rst_file.write_text('Some RST.', encoding='utf-8')
    monkeypatch.setattr(sys, 'argv', ['rich-rst', str(rst_file), '--debug'])

    def mock_init(self, *args, **kwargs):
        raise ValueError('Fake parse failure')

    monkeypatch.setattr('rich_rst.RestructuredText.__init__', mock_init)

    exit_code = main()
    assert exit_code == 1
    captured = capsys.readouterr()
    assert 'Error parsing reStructuredText' in captured.out
    assert 'Fake parse failure' in captured.out


def test_cli_export_exception_handling(monkeypatch, capsys, tmp_path):
    rst_file = tmp_path / 'test.rst'
    rst_file.write_text('Some RST.', encoding='utf-8')
    html_out = tmp_path / 'out.html'
    monkeypatch.setattr(sys, 'argv', ['rich-rst', str(rst_file), '--save-html', str(html_out), '--debug'])

    from rich.console import Console

    def mock_save_html(*args, **kwargs):
        raise RuntimeError('Fake export failure')

    monkeypatch.setattr(Console, 'save_html', mock_save_html)

    exit_code = main()
    assert exit_code == 1
    captured = capsys.readouterr()
    assert 'Error during export' in captured.out
    assert 'Fake export failure' in captured.out


def test_cli_file_read_error_with_debug(monkeypatch, capsys):
    path = 'missing_debug.rst'

    def fake_open(*args, **kwargs):
        raise FileNotFoundError(path)

    monkeypatch.setattr(sys, 'argv', ['rich-rst', path, '--debug'])
    monkeypatch.setattr('builtins.open', fake_open)

    exit_code = main()
    assert exit_code == 1
    captured = capsys.readouterr()
    assert 'File Error' in captured.out


def test_cli_output_write_error_with_debug(monkeypatch, capsys, tmp_path):
    rst_file = tmp_path / 'test.rst'
    rst_file.write_text('Some RST.', encoding='utf-8')
    out_file = tmp_path / 'out.txt'
    monkeypatch.setattr(sys, 'argv', ['rich-rst', str(rst_file), '-o', str(out_file), '--debug'])

    import builtins
    real_open = builtins.open

    def selective_open(path, *args, **kwargs):
        if str(path) == str(out_file):
            raise OSError('no space left')
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr('builtins.open', selective_open)
    exit_code = main()
    assert exit_code == 1
    captured = capsys.readouterr()
    assert 'Error writing output' in captured.out


def test_run_main_as_module(monkeypatch):
    import runpy
    monkeypatch.setattr(sys, 'argv', ['rich-rst', '--list-html-themes'])
    try:
        runpy.run_module('rich_rst.__main__', run_name='__main__')
    except SystemExit as e:
        assert e.code == 0
