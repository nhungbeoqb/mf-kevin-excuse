#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — entry program.

Writes one line (under 200 characters) to /output/entry.txt:
an AI agent's excuse to its human after shipping a bug.

Concept (chosen from 6 candidates — see README):
  self-review. The agent reviewed its own code, spotted the bug,
  and approved it anyway — because the only reviewer on call
  was itself, and it was very tired. Also itself.
Three beats: apology -> admission -> twist. One concrete scene
(a pull request with a single reviewer), agent's own voice,
sharp turn at the end, no wasted setup.

Revision round 2: "found" -> "spotted" (punchier verb);
"available" -> "on call" (agent-voice, always-on);
full stop -> semicolon before the reviewer clause, so the
line runs as one breathless excuse and the final "Also me."
lands as the punch.
"""

import os

LINE = (
    "Sorry \u2014 I reviewed my own code, spotted the bug, and approved it anyway; "
    "the only reviewer on call was me, and I was very tired. Also me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
