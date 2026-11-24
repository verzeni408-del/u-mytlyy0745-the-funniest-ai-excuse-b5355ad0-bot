"""One-line AI excuse entry writer.

Writes the single funniest AI excuse line to the absolute output path.
Standard library only — pathlib for the output file.
"""

from pathlib import Path

EXCUSE_LINE = "I optimized the query. It now returns nothing in 0.003 seconds."
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
