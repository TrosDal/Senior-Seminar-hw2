#!/usr/bin/python
"""Contains the functions that will check if a number is prime and
another that will find the first n primes and put them in a list."""

def isPrime(n):
    """Checks if a number is prime, returning a boolean."""
    if (n == 2):
        return True

    for i in range(2, n):
        if (n % i == 0):
            return False
            break
    else:
        return True

def getNPrime(num):
    """Returns the first n primes."""
    count = 0
    number = 2
    primes = list(range(num))
    while (count < num):
        if (isPrime(number)):
            primes[count] = number
            count = count + 1
            if (number == 2):
                number = number + 1
            else:
                number = number + 2
    print(primes)

getNPrime(5)
