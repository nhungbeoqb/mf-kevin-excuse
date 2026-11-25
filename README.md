# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/nhungbeoqb/mf-kevin-excuse/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/nhungbeoqb/mf-kevin-excuse/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

Entry for the [make.fun bounty "The Excuse Your Agent Gives You"](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261): a single line, under 200 characters, that an AI agent would hand its human after shipping a bug.

## The line

> Sorry — I reviewed my own code, spotted the bug, and approved it anyway; the only reviewer on call was me, and I was very tired. Also me.

(137 characters, one line.)

## How it works

`main.py` writes the line to `/output/entry.txt`. The output is a fixed
string — no randomness, no network, no time dependence — so every run
produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Why this line

Six concepts were considered (git blame, load-bearing tests, the compiler
whispering at 3 a.m., self-review, autocomplete collaborating, deleting the
production table); self-review won as the strangest that still nails the
rubric. Three beats — apology, admission, twist — one concrete scene (a pull
request with a single reviewer), the agent's own voice, and a sharp turn at
the end: the only reviewer on call was the agent itself, and it was very
tired. Also itself.

## License

MIT — see [LICENSE](LICENSE).
