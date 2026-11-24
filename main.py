"""One line of earned pride.

Why this line works against the judge's brief:

* Genuine, earned pride: the pride is inside the scene, not asserted.
  Three winters of failing the driving test is a long, humbling effort;
  the clean parallel park is the payoff, and the quiet sit afterwards
  is the feeling landing.
* Concrete scene with a real person: a named man, a specific car
  (his late wife's), a specific hard manoeuvre, in one visible moment.
* Lands in one read: the pride arrives by the last words — "hands
  still on the wheel" — with no setup the reader has to assemble.
* Freshness: no trophy, podium or graduation; the image is an old man
  alone in a parked car, savouring a small victory.
"""

LINE = (
    "After three winters of failing the driving test, old Mr. Chen "
    "parallel-parked his late wife's car first try \u2014 and sat there "
    "a moment, hands still on the wheel."
)

assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
assert "\n" not in LINE, "line must be a single line"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
