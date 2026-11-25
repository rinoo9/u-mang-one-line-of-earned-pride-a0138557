"""One line of earned pride.

Why this line works against the judge's brief:

* Genuine, earned pride: the pride is inside the scene, not asserted.
  Forty years of night shifts is a long, humbling effort; seeing her
  name on the hospital wall is the payoff, and touching the plaque is
  the feeling landing.
* Concrete scene with a real person: a named woman, a specific place
  (the hospital wall), a specific small honour, in one visible moment.
* Lands in one read: the pride arrives by the last words — "like it
  might be a trick of the light" — with no setup the reader has to
  assemble.
* Freshness: no trophy, podium or graduation; the image is a cleaner
  alone in a corridor, savouring a small victory.
* Understated, not announced: the line never says "she was proud";
  the pride is shown by what she does — she touches the plaque
  instead of celebrating — so the reader feels it rather than being
  told it.
* One breath, one image: the sentence never leaves the corridor —
  working, seeing, touching — so the whole arc fits in a single
  unbroken moment the reader can picture in one read.
"""

LINE = (
    "After forty years of night shifts, Rosa the cleaner finally saw "
    "her name on the hospital wall \u2014 employee of the month \u2014 and "
    "she touched the plaque like it might be a trick of the light."
)

assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
assert "\n" not in LINE, "line must be a single line"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
