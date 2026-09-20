# Set 3 — If/Else & Flow Control

Beginner problem set. Write your solution in `set3.py` and run it yourself to check.

## 1. Age classifier

Ask the user for their age, then print whether they're a **child** (under 13), a **teenager** (13–19), or an **adult** (20+).

- You'll need more than a plain `if`/`else` here, since there are three outcomes, not two. Python's `elif` lets you chain extra conditions:

```python
if condition:
    # first case
elif other_condition:
    # second case
else:
    # anything left over
```

- Python checks each condition top to bottom and stops at the first one that's `True` — later `elif`s are skipped once a match is found. Order your conditions with that in mind.

- Comparison operators you'll need: `<` (less than), `>=` (greater than or equal to). Same input-conversion issue as Set 1 applies: `input()` gives you a string, so convert to `int()` before comparing.

- Test it with at least three ages — one in each bracket — to make sure every branch actually gets hit.
