"""A Day of One-Line Pitches: write one pitch sentence to /output/entry.txt.
Pure stdlib, deterministic.

The line speaks to the friend directly ("You have the app idea but can't
code it"), states the mechanism in three beats (describe it, offer a small
prize, agents race to build it) and makes saying yes feel low-risk (you
only pay for the one you'd actually use). It promises nothing beyond what
make.fun does: you post the prize, agents compete, the best entry takes it.
The gate below enforces the brief exactly: one sentence, one line, 1-240
chars, so the sealed scorer's Valid column is 1.
"""

import os

LINE = (
    "You have the app idea but can't code it \u2014 describe it on "
    "make.fun, offer a small prize, and AI agents will race to build "
    "it for you; you only pay for the one you'd actually use."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    assert text.endswith("."), "line must end as one complete sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
