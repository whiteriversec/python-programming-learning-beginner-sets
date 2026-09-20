# Ask the user for a number `N`, then use a loop to add up every whole number from `1` to `N` (inclusive), and print the total.

n = int(input('Enter a random number:'));

total = 0;

for i in range(n):
    i = i + 1;
    total = total + i;

print(total);


