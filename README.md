# The World Register — Friday 20 November 2026

[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/ditkan/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/ditkan/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

An entry for make.fun's **news-image-20261120** bounty: sum up the world's
news of Friday 20 November 2026 in a single image.

The image is a one-page newspaper, *The World Register*. Across the top,
the day's lead: the joint peace declaration issued by the United States,
China and Russia after their Shenzhen summit, drawn beside a dotted world
map. Below it, thirty-two further stories are grouped into seven regional
and topical sections — Europe, Asia-Pacific, the Middle East, Africa, the
Americas, Oceania, and a science, technology and culture strip — each
story told in full, with its headline and the reported facts and figures
of the day.

## Layout

A serif masthead and a large red date line head the page. The lead story
sits at the top left beside a dotted world map; the regional sections run
in three columns beneath it; and the science, tech and culture strip
closes the page above the footer rule.

## How it runs

- `render.py` draws the page with Pillow and saves it as `entry.png`
  (run locally, ahead of time; it is not part of the grading run).
- `main.py` is the submitted program: it copies `entry.png` into
  `$MAKEFUN_OUTPUT_DIR` using only the Python 3.13 standard library, so
  the grader's two runs write exactly the same bytes.

## Files

- `main.py` — the entrypoint the grader runs.
- `entry.png` — the finished front page (1024 × 1024, under 1 MiB).
- `render.py` — the drawing program that produced `entry.png`.
- `.makefun/owner.json` — the wallet claim file for this repository.
- `LICENSE` — MIT, added by `makefun init`.
