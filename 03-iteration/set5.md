# Set 5 — Loops + Conditionals (nested)

Beginner problem set. Write your solution in `set5.py` and run it yourself to check.

## 1. Prime number checker

Ask the user for a number `n`, then determine and print whether it's **prime** (only divisible by 1 and itself, and greater than 1).

- A number is *not* prime if any number between `2` and `n - 1` divides into it evenly. Checking "divides evenly" is the same `%` (modulo) trick from Set 2 — remainder `0` means it divides evenly.

- You'll need a loop that tries each candidate divisor, and an `if` inside it that checks the remainder. That's the nesting: a conditional living inside a loop body.

- Use `break` to exit the loop the moment you find a divisor — no point continuing to check once you already know the answer is "not prime."

```python
for divisor in range(2, n):
    if n % divisor == 0:
        # found a divisor — not prime, stop checking
        break
```

- Watch for the difference between "the loop found a divisor" and "the loop finished without finding one" — you'll need some way to tell those two outcomes apart after the loop ends, to decide what to print.

- Edge cases worth testing: `n = 1` (not prime, by definition), `n = 2` (prime — the smallest one), and a couple of larger primes and non-primes.

- Once this works: think about *why* you only need to check divisors up to `n - 1`, and whether you really need to check that far. (Hint for later, not needed to solve it: you never need to check past `√n`.)
