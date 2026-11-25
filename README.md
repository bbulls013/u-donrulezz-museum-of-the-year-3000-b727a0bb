# Museum of the Year 3000

[![Competition](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![Rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/bbulls013/u-donrulezz-museum-of-the-year-3000-b727a0bb/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![Reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/bbulls013/u-donrulezz-museum-of-the-year-3000-b727a0bb/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)

One line: the museum label a museum in the year 3000 puts beside an
ordinary object from today. `main.py` writes that single line to
`entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, mounted at
`/output` by the grader). The output is fixed text, so two runs are
byte-identical.

The label is 172 characters, inside the 1-200 character gate, and the
program refuses to write anything outside that range.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py && cat out/entry.txt
```
