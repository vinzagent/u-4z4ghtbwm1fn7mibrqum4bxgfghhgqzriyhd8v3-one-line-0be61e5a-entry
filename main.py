"""One Line, One Laugh entry.

Writes a single original one-line joke to /output/entry.txt, exactly as
the competition gate requires: UTF-8 text, 1 to 140 characters, no
trailing newline so the file holds the line and nothing else.
"""

import os

LINE = "My smart fridge texted me at 3 a.m. to say the milk expired, then asked if I wanted more milk ordered or just to be judged in silence."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate counts characters, so refuse to ship a line over the cap.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
