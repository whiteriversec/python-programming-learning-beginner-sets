# Set 8 — Strings

Beginner problem set. Write your solution in `set8.py` and run it yourself to check.

## 1. Vowel counter

Ask the user for a word (or sentence), then count how many vowels (`a`, `e`, `i`, `o`, `u` — both upper and lowercase) it contains, and print the count.

```python
word = input("Enter a word: ")
```

- This is the same character-by-character traversal you used in Set 7's password checker — `for char in word:` — but the pattern itself is different. Set 7 asked "does *at least one* character satisfy this?" (a flag). This asks "*how many* characters satisfy this?" — that's a **counter**, the same accumulator idea from Set 4's running total, just incrementing by `1` instead of adding a variable amount.

- New tool worth using here: the `in` operator lets you check membership directly, instead of chaining `or` comparisons. `if char in 'aeiouAEIOU':` reads almost like English, and does exactly what five separate `==` checks chained with `or` would do.

- Strings are case-sensitive — `'A' == 'a'` is `False`. You can sidestep this entirely by calling `.lower()` on the input once at the start, then only checking against lowercase vowels — one less thing to worry about for the rest of the function.

- Edge cases worth testing: an empty string (`''`), a word with no vowels at all (`'gym'`), and a word that's all vowels (`'aeiou'`).

- Once it works: turn it into a function, `count_vowels(text)`, that **returns** the count instead of printing it directly — same return-vs-print distinction from Set 7, now handing back a count instead of a `True`/`False`.
