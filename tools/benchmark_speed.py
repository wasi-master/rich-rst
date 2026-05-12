#!/usr/bin/env python3
"""Benchmark rich-rst rendering speed with standard Rich vs experimental fast-rich."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DEFAULT_INPUT = REPO_ROOT / "docs" / "source" / "_extra" / "specification.txt"

_SNIPPET = r"""
from __future__ import annotations
import json
import io
import statistics
import sys
import time
from contextlib import redirect_stdout
from pathlib import Path

path = Path(sys.argv[1])
multiplier = int(sys.argv[2])
iterations = int(sys.argv[3])
width = int(sys.argv[4])

content = path.read_text(encoding="utf-8")
large_rst = ("\n\n" + ("=" * 80) + "\n\n").join([content] * multiplier)

from rich_rst import RestructuredText

times = []
for _ in range(iterations):
    start = time.perf_counter()
    with redirect_stdout(io.StringIO()):
        RestructuredText(large_rst).render_to_string(width=width)
    times.append(time.perf_counter() - start)

print(json.dumps({
    "mean": statistics.mean(times),
    "median": statistics.median(times),
    "min": min(times),
    "max": max(times),
    "iterations": iterations,
    "chars": len(large_rst),
}))
"""


def run_backend(input_file: Path, multiplier: int, iterations: int, width: int, backend: str) -> dict:
    env = os.environ.copy()
    env["RICH_RST_USE_FAST_RICH"] = "1" if backend == "fast-rich" else "0"
    command = [
        sys.executable,
        "-c",
        _SNIPPET,
        str(input_file),
        str(multiplier),
        str(iterations),
        str(width),
    ]
    result = subprocess.run(command, cwd=REPO_ROOT, env=env, check=True, capture_output=True, text=True)
    return json.loads(result.stdout.strip())


def build_unicode_stress_file() -> Path:
    row = "| 列一 😀😀😀 | 列二 αβγδεζηθ | 列三 你好世界 |\n"
    parts = []
    for i in range(1200):
        parts.append(f"Section {i}\n---------\n\n")
        parts.append(row * 3)
        parts.append("\n这是一些包含宽字符和emoji 😀😄😁 的文本，用于压力测试。\n\n")
    handle = tempfile.NamedTemporaryFile(prefix="rich-rst-bench-", suffix=".rst", delete=False)
    path = Path(handle.name)
    handle.close()
    path.write_text("".join(parts), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--preset",
        choices=("specification", "unicode-stress"),
        default="specification",
        help="Benchmark input preset",
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help=f"RST file path (default: {DEFAULT_INPUT})")
    parser.add_argument("--multiplier", type=int, default=6, help="How many times to repeat the RST input to make a large document")
    parser.add_argument("--iterations", type=int, default=7, help="Benchmark iterations per backend")
    parser.add_argument("--width", type=int, default=120, help="Render width")
    args = parser.parse_args()

    if args.preset == "unicode-stress":
        input_file = build_unicode_stress_file()
    else:
        input_file = args.input

    if not input_file.exists():
        raise SystemExit(f"Input file not found: {input_file}")

    has_fast_rich = importlib.util.find_spec("fast_rich") is not None

    rich_stats = run_backend(input_file, args.multiplier, args.iterations, args.width, "rich")
    print(f"Preset: {args.preset}")
    print(f"Input chars: {rich_stats['chars']:,}")
    print(f"Iterations: {rich_stats['iterations']}")
    print()
    print("| Backend | Mean (s) | Median (s) | Min (s) | Max (s) |")
    print("|---|---:|---:|---:|---:|")
    print(
        f"| rich | {rich_stats['mean']:.4f} | {rich_stats['median']:.4f} | {rich_stats['min']:.4f} | {rich_stats['max']:.4f} |"
    )

    if has_fast_rich:
        fast_stats = run_backend(input_file, args.multiplier, args.iterations, args.width, "fast-rich")
        print(
            f"| fast-rich | {fast_stats['mean']:.4f} | {fast_stats['median']:.4f} | {fast_stats['min']:.4f} | {fast_stats['max']:.4f} |"
        )
        improvement = (rich_stats["mean"] - fast_stats["mean"]) / rich_stats["mean"] * 100.0
        print()
        print(f"Mean speed improvement with fast-rich: {improvement:.2f}%")
    else:
        print()
        print("fast-rich is not installed; benchmarked only standard rich.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
