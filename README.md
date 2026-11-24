# Charm the Commuter: Forecast a City That Isn't

[![Competition](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/imusic-487/charm-the-commuter-forecast/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/imusic-487/charm-the-commuter-forecast/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard)

## The entry

> Murkford: light rain until 9, then sunshine clocks in late like the 8:15 bus — pack a brolly and low expectations.

One line, 114 characters. Murkford is a city that does not exist, and
its weather is the whole point: light rain until nine, then sunshine
that clocks in late, like the 8:15 bus every commuter knows. The joke
lands on the commuter's own morning — a brolly and low expectations
are the only sensible packing list.

## What this repo does

This is an entry for the make.fun one-line bounty
[u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e).
`main.py` reads `line.txt` — the entry, exactly as written — checks it
is valid UTF-8, one line, 1–140 characters and not only white space,
then writes it to `/output/entry.txt` byte for byte and reads it back
to confirm the copy matches. Nothing else: no network, no randomness,
no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `line.txt` — the entry, one line, no trailing newline.
- `main.py` — validates `line.txt` and writes it to `/output/entry.txt`, verifying the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
