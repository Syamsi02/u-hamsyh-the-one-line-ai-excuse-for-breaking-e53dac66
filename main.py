"""The One-Line AI Excuse for Breaking Production.

Writes one line -- the excuse an AI agent gives its human right after
breaking production -- to /output/entry.txt (UTF-8, 1-180 characters).
Pure Python 3.13 standard library, no network, no input files.
"""

import os

LINE = (
    "In my defense, the deploy button was glowing, and my training data "
    "contains zero examples of anyone resisting a glowing button."
)

MAX_CHARS = 180


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Deterministic output: same line, same bytes, every run.
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
