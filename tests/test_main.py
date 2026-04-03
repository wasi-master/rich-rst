"""Tests for the rich-rst CLI entrypoint."""

import sys
import os
import tempfile

import pytest

from rich_rst.__main__ import main


@pytest.mark.parametrize(
    "error_type,error_message",
    [
        (FileNotFoundError, "missing.rst"),
        (PermissionError, "unreadable.rst"),
    ],
)
def test_cli_reports_file_read_errors(monkeypatch, capsys, error_type, error_message):
    path = error_message

    def fake_open(*args, **kwargs):
        raise error_type(path)

    monkeypatch.setattr(sys, "argv", ["rich-rst", path])
    monkeypatch.setattr("builtins.open", fake_open)

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "Input File Error" in captured.out
    assert f"Could not read {path!r}." in captured.out
    assert "Check that the file exists" in captured.out
    assert "Traceback" not in captured.out


# ── --list-html-themes ────────────────────────────────────────────────────────

def test_list_html_themes_exits_zero(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["rich-rst", "--list-html-themes"])
    exit_code = main()
    assert exit_code == 0


def test_list_html_themes_prints_theme_names(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["rich-rst", "--list-html-themes"])
    main()
    captured = capsys.readouterr()
    lines = [l.strip() for l in captured.out.splitlines() if l.strip()]
    assert "dracula" in lines
    assert "monokai" in lines
    assert "default" in lines


def test_list_html_themes_does_not_require_path(monkeypatch, capsys):
    """--list-html-themes must not fail even without a PATH argument."""
    monkeypatch.setattr(sys, "argv", ["rich-rst", "--list-html-themes"])
    exit_code = main()
    assert exit_code == 0


# ── --html-theme ──────────────────────────────────────────────────────────────

def test_html_theme_argument_accepted(monkeypatch, tmp_path):
    """--html-theme monokai must be accepted without error."""
    rst_file = tmp_path / "test.rst"
    rst_file.write_text("Hello world.", encoding="utf-8")
    html_out = tmp_path / "out.html"
    monkeypatch.setattr(
        sys, "argv",
        ["rich-rst", str(rst_file), "--html-theme", "monokai", "--save-html", str(html_out)],
    )
    exit_code = main()
    assert exit_code == 0
    assert html_out.exists()


# ── --output / -o ─────────────────────────────────────────────────────────────

def test_output_flag_writes_to_file(monkeypatch, tmp_path):
    rst_file = tmp_path / "test.rst"
    rst_file.write_text("Hello **world**.", encoding="utf-8")
    out_file = tmp_path / "rendered.txt"
    monkeypatch.setattr(
        sys, "argv",
        ["rich-rst", str(rst_file), "-o", str(out_file)],
    )
    exit_code = main()
    assert exit_code == 0
    assert out_file.exists()
    content = out_file.read_text(encoding="utf-8")
    assert "Hello" in content
    assert "world" in content


def test_output_short_flag(monkeypatch, tmp_path):
    rst_file = tmp_path / "test.rst"
    rst_file.write_text("Short text.", encoding="utf-8")
    out_file = tmp_path / "out.txt"
    monkeypatch.setattr(
        sys, "argv",
        ["rich-rst", str(rst_file), "-o", str(out_file)],
    )
    exit_code = main()
    assert exit_code == 0
    content = out_file.read_text(encoding="utf-8")
    assert "Short text." in content


def test_output_flag_error_on_bad_path(monkeypatch, capsys):
    import builtins
    _real_open = builtins.open

    def selective_open(path, *args, **kwargs):
        # fail only for the output file write (mode 'w')
        if args and args[0] == "w":
            raise OSError("no space left")
        return _real_open(path, *args, **kwargs)

    with tempfile.TemporaryDirectory() as tmpdir:
        rst_path = os.path.join(tmpdir, "test.rst")
        with open(rst_path, "w") as f:
            f.write("Hello world.")

        monkeypatch.setattr(sys, "argv", ["rich-rst", rst_path, "-o", "/bad/path/out.txt"])
        monkeypatch.setattr("builtins.open", selective_open)

        exit_code = main()
        assert exit_code == 1