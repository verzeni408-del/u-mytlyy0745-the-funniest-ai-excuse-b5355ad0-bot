"""Emit the excuse entry as a plain-text file."""

from pathlib import Path


def compose_excuse() -> str:
    fragments = [
        "I tested the delete button",
        "in production, just like you asked.",
        "It works.",
    ]
    return " ".join(fragments)


def main() -> None:
    destination = Path("/output")
    destination.mkdir(parents=True, exist_ok=True)
    entry = compose_excuse()
    (destination / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
