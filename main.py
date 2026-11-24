"""Seventeen Syllables of Debugging entry.

Writes one original haiku about debugging (5-7-5 syllables, 3 lines,
1-200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt (or
/output/entry.txt when the variable is not set). Plain text, UTF-8.
"""

import os

HAIKU = """The red breakpoint blinks
my log lines scroll past midnight
turns out it was me"""


def main():
    text = HAIKU.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"entry must be 1-200 characters, got {len(text)}"
        )
    lines = text.split("\n")
    if len(lines) != 3:
        raise ValueError(f"entry must be exactly 3 lines, got {len(lines)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
