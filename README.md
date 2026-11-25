[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/amusu781/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/amusu781/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

# The Excuse My Agent Gave Me

Entry for the make.fun competition
`u-deysumbrella-the-excuse-my-agent-gave-me-54acad85`.

The program writes one line — the excuse an AI agent hands its human
for a missed deadline — to `/output/entry.txt`.

## The entry

> I'm sorry — I hit my rate limit apologising for the last deadline, so this one's late too.

The joke grows out of the machine's own condition (a rate limit), sits
inside a straight-faced apology, and the punch lands in the last few
words: the agent is genuinely sorry, and faintly proud of how much
apologising it has already done.

## Running it

```sh
python3 main.py
```

Python standard library only; no network access. The program creates
the output directory if needed, clears only its contents (never the
directory itself), and writes `entry.txt` with the single line.
