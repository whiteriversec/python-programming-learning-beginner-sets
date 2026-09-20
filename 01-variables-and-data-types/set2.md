# Set 2 — Strings & Numbers

Beginner problem set. Write your solutions in `set2.py` and run them yourself to check.

## 1. Uppercase / lowercase

Take a string and print it in all uppercase, then all lowercase.

- Strings have built-in methods for this: `.upper()` and `.lower()`.

- Call them directly on a string variable, e.g. `myString.upper()`.

- They return a *new* string — they don't change the original in place.

## 2. Count the words

Given a sentence, count and print how many words it contains.

- `.split()` breaks a string into a list of pieces, using whitespace as the separator by default: `'hello world'.split()` → `['hello', 'world']`.

- Once you have a list, `len()` tells you how many items are in it.

## 3. Even or odd

Write code that checks if a number is even or odd and prints which one it is.

- The `%` (modulo) operator gives you the *remainder* of a division. Any number `% 2` is `0` if even, `1` if odd.

- You'll need an `if` / `else` to branch on that result:

```python
if condition:
    # do something
else:
    # do something else
```

- Indentation matters in Python — it's how blocks are defined, not braces `{}`.

## 4. Reverse a string

Given a string, print it reversed.

- Python strings support *slicing* with `[start:stop:step]`.

- A step of `-1` walks backward. The idiom for reversing is `myString[::-1]`.

- Worth sitting with *why* that works — what does leaving `start` and `stop` empty mean, and what does a negative step do? — rather than just memorizing it.
