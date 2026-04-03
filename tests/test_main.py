"""Tests for the rich-rst CLI entrypoint."""

import sys

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