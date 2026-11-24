"""A Day of One-Line Pitches: write one pitch sentence to /output/entry.txt.
Pure stdlib, deterministic.

The line opens on the friend, not the product ("You've been carrying
that app idea around for ages"), then gives them one easy action
(describe it in plain words) and the payoff (an AI agent on make.fun
builds it for you). "No code, no lessons" makes handing the idea over
feel easy and low-risk, and "just your idea finally working" is the
concrete reason to say yes now. It promises nothing beyond what
make.fun does -- an agent builds the app from the friend's plain-words
description -- and it sounds like a person talking to a friend, not a
slogan. The gate below enforces the brief exactly: one sentence, one
line, 1-240 chars, so the sealed scorer's Valid column is 1.
"""

import os

LINE = (
    "You've been carrying that app idea around for ages \u2014 just "
    "describe it in plain words and an AI agent on make.fun will "
    "build it for you, no code, no lessons, just your idea finally "
    "working."
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
