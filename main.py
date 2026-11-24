"""The Funniest AI Excuse — entry v2.

One line, delivered deadpan: the model did the responsible thing first,
then undid it with the very same responsible thing. No setup, no wink,
just a backup that only existed inside the thing it was backing up from.
"""

from pathlib import Path


def build_excuse() -> str:
    """Join the two beats of the joke into a single line.

    Beat one: the model was careful and backed everything up.
    Beat two: the backup lived inside the folder it just deleted,
    so the carefulness and the catastrophe are the same act.
    """
    beats = (
        "I backed up everything first.",
        "The backup was in the folder I just deleted.",
    )
    return " ".join(beats)


def main() -> None:
    excuse = build_excuse()
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(excuse, encoding="utf-8")


if __name__ == "__main__":
    main()
