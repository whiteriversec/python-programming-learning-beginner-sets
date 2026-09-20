# User inputs a number, program checks if its a prime number.

n = int(input('Enter a number: '));

is_prime = True   # assume it's prime until proven otherwise

for divisor in range(2, n):
    if n % divisor == 0:
        is_prime = False   # found a divisor — assumption was wrong
        break               # no point checking further

if is_prime:
    print('Is a prime')
else:
    print('Not a prime')