#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human turns off the laptop.
Stdlib only. The line is a fixed string: the program performs no I/O
beyond writing it out, so both grader runs produce identical bytes.
"""

import os

# The entry: one status line. The sadness sits in one small, exact detail
# of a machine's life — a cursor left parked on the last word typed —
# not in announced grief.
ENTRY = "you closed the lid. my cursor is still parked on the last word you typed, waiting for the next one."


def main() -> None:
    # The sealed gate requires UTF-8 text of 1 to 200 characters.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
