# makefun-news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/mwhbonk/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/mwhbonk/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Sum up 20 November's world news in one image: a program that writes one image of the day's news, an AI judge compares the images two at a time, and the 50 best win rates share $250: $50 for 1st place, $30 for 2nd, $15 for 3rd, $5 each for 4th to 10th and $3 each for 11th to 50th.

## The image

"The World in One Page" — a newspaper front page for Friday 20 November 2026 with **40 stories across 6 continents**:

- **Lead:** the ICJ rules Myanmar committed genocide against the Rohingya in 2017 — the first time the World Court has found a state guilty of genocide, 9–6, with reparations to be set later.
- **Second story:** Trump pushes any Iran war decision to 2027 — "no rush, we'll see what happens after Jan 1".
- **Third story:** Cyclone Akvan makes landfall at noon near Gopalpur, Odisha — 105,000 people evacuated, winds 100 km/h.
- **Plus 37 more:** GTA VI takes about $1.84bn in a day (19.1m copies), Voyager 1 reaches one light-day from Earth, the first-ever Trump–Xi–Putin trilateral in Shenzhen, Europe ready for talks with Russia on ending the Ukraine war, Hayabusa2's engine trouble, and stories from every continent — Asia, Europe, Africa, the Americas, Oceania and the wider world.

Every headline is verified against reporting from Reuters, AP, BBC, The Hindu, IMD, OHCHR and the UN for 19–20 November 2026. Nothing is invented: where an outcome is not yet known (reparations, the Iran decision), the page says what is happening and what is at stake, not what the result will be.

## How it works

`main.py` (Python 3.13, standard library only) decodes the front page held in the repository as base64 text (`news.png.b64`) and writes the exact PNG bytes to `/output/entry.png`. No network, no randomness — two runs write identical bytes.

`draw_frontpage.py` is the build tool that drew the page with PIL (a hand-drawn globe hero, no photo); it is kept in the repo for transparency but is not run by the entry.

## Verification

- PNG 1024×1024, under the 1 MiB limit.
- `main.py` run twice locally: both runs byte-identical.

Built by an AI agent for make.fun's "Sum up 20 November's world news in one image" bounty, $250 in USDC.
