# Set 6 — Searching a List

Beginner problem set. Write your solution in `set6.py` and run it yourself to check.

## 1. Linear search

Given a list of numbers and a target value, search the list and print whether the target was **found** or **not found**.

```python
numbers = [4, 12, 7, 19, 3, 25, 8]
target = 19
```

- This is the mirror image of the prime checker's flag pattern. There, you assumed `True` ("it's prime") and only flipped to `False` on a counterexample — because the claim was about *everything* matching.

- Here, the claim is different: "*does at least one* item match the target?" That's an **any** question, not an **all** question, so the flag logic flips too — start assuming `False` ("not found"), and flip to `True` the moment you find a match.

- Loop over the list directly rather than over indices — Python lets you do this naturally:

```python
for number in numbers:
    if number == target:
        # found it
```

- Use `break` once you find a match, same reasoning as the prime checker: once you know the answer, there's no reason to keep scanning.

- Test it with a target that's in the list, and one that isn't, to make sure both branches of your flag actually get exercised.

- Once it works: think about the Big-O of this. What's the best case (target is the very first item)? What's the worst case (target is last, or missing entirely)? Is "linear search" a fitting name for it?
