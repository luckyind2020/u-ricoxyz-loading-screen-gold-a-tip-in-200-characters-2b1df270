"""Loading Screen Gold — print the one-line loading-screen tip.

The tip itself lives in entry.txt so the text stays a single,
judge-readable line; this runner only loads it and prints it.
"""

from pathlib import Path


def load_tip() -> str:
    tip_path = Path(__file__).resolve().parent / "entry.txt"
    tip = tip_path.read_text(encoding="utf-8").strip()
    if "\n" in tip:
        raise ValueError("entry must be a single line")
    if len(tip) > 200:
        raise ValueError("entry exceeds the 200-character limit")
    return tip


def main() -> None:
    print(load_tip())


if __name__ == "__main__":
    main()
