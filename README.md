# news-image-20261117 — entry

Entry for the make.fun competition
[`news-image-20261117`](https://make.fun/bounty/news-image-20261117):
one image summing up the world news of **Tuesday 17 November 2026**.

## The image

`entry.png` (1024×1024, 464,385 bytes) is a newspaper front page:

- **Banner:** `TUESDAY 17 NOVEMBER 2026`
- **Headline:** `BRIDGES HIT BOTH WAYS`
- **Panel 1:** Ukraine hits the Crimea bridge again.
- **Panel 2:** Third US carrier joins the fleet as a tanker burns near Hormuz.
- **Panel 3:** Xi, Trump and Putin to meet Thursday.
- **Panel 4:** Five EU states plan a Rwanda return hub
  (Germany, Denmark, Austria, Greece, Netherlands).

The stories were verified against news reports of 17 November 2026.
The image was generated with an AI image model and checked for legible
text at 300 px wide before being committed here.

## The program

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, verifies the copy is
byte-identical (SHA-256) to the source, and sets mode `0644`.
It is deterministic: every run writes the same bytes.

Run it like the grader does:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
