"""Seventeen Syllables of Debugging entry.

Writes one original haiku about debugging (5-7-5 syllables, 3 lines,
1-200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt (or
/output/entry.txt when the variable is not set). Plain text, UTF-8.
Standard library only.
"""

import os

HAIKU_LINES = (
    "The red breakpoint blinks",
    "my log lines scroll past midnight",
    "turns out it was me",
)

MIN_CHARS = 1
MAX_CHARS = 200
EXPECTED_LINES = 3


def join_lines(lines):
    """Join the haiku lines into a single text block."""
    return "\n".join(lines)


def check_length(text):
    """Require the entry to be within the allowed character range."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )


def check_line_count(text):
    """Require the entry to be exactly three lines."""
    count = len(text.split("\n"))
    if count != EXPECTED_LINES:
        raise ValueError(
            "entry must be exactly %d lines, got %d"
            % (EXPECTED_LINES, count)
        )


def validate(text):
    """Run every entry check before anything is written."""
    check_length(text)
    check_line_count(text)


def resolve_output_dir():
    """Pick the grader output dir, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def entry_path(out_dir):
    """Build the full path of the file to write."""
    return os.path.join(out_dir, "entry.txt")


def write_entry(path, text):
    """Create the parent dir if needed and write the entry."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def build_entry():
    """Assemble and validate the haiku text."""
    text = join_lines(HAIKU_LINES)
    validate(text)
    return text


def main():
    text = build_entry()
    path = entry_path(resolve_output_dir())
    write_entry(path, text)


if __name__ == "__main__":
    main()
