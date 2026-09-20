# Set 4 — Loops

Beginner problem set. Write your solution in `set4.py` and run it yourself to check.

## 1. Sum from 1 to N

Ask the user for a number `N`, then use a loop to add up every whole number from `1` to `N` (inclusive), and print the total.

- Python's `for` loop pairs naturally with `range()`: `range(1, n + 1)` produces `1, 2, 3, ..., n`. Note the `+ 1` — `range()`'s upper bound is *exclusive*, so leaving it off would stop one short of `n`.

- You'll need an accumulator: a variable that starts at `0` before the loop, then gets added to on every pass through it.

```python
total = 0
for number in range(1, n + 1):
    total = total + number
```

- Same input-conversion rule as before: `input()` gives you a string, so `int()` it before using it in `range()`.

- Check your answer against the shortcut formula for this problem, `n * (n + 1) / 2` — if your loop's result doesn't match it for a few different `n` values, something's off.
