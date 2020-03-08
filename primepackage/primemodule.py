#!/usr/bin/python
"""Contains the functions that will check if a number is prime and
another that will find the first n primes and put them in a list."""

def is_prime(num):
    """Determines if the supplied number is prime, returning True or False."""
    if num == 2:
        return True

    numbers = range(2, num)

    for i in numbers:
        if num % i == 0:
            return False

    return True

def get_n_prime(num):
    """Returns the first n primes."""
    count = 0
    number = 2
    primes = []
    while count < num:
        if is_prime(number):
            primes.append(number)
            count = count + 1
        if number == 2:
            number = number + 1
        else:
            number = number + 2
    return primes
