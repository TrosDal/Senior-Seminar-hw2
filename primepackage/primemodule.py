#!/usr/bin/python
"""Contains the functions that will check if a number is prime and
another that will find the first n primes.

This module contains the function "is_prime", which returns true
if the supplied number is prime and false otherwise.
It also contains the function "get_n_prime", whic hreturns the first n
prime numbers, using "is_prime" to check.
"""

__author__ = "Rene Zambrana"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "rxzambrana@valdosta.edu"
__status__ = "Prototype"

def is_prime(num):
    """Determines if the supplied number is prime, returning True or False.

    Args:
        num (int): integer to be checked.

    Returns:
        boolean: True if prime, False if not.

    Raises:
        TypeError: When a non-integer value is supplied.

    Examples:
        >>>> check = is_prime(77);
    """
    if num <= 0:
        raise ValueError('Number being checked for prime-ness must be positive.')

    if num == 2:
        return True

    numbers = range(2, num)

    for i in numbers:
        if num % i == 0:
            return False

    return True

def get_n_prime(num):
    """Returns the first n primes, using "is_prime" to check for primeness.

    Args:
        num (int): number of primes to be added to the returned list.

    Returns:
        list (int): Returns a list of the first "num" prime integers.

    Raises:
        ValueError: When an integer less than 1 is supplied.
        TypeError: When a non-intger value is supplied.
    Examples:
        >>>> primes = get_n_prime(20);
    """
    if num < 0:
        raise ValueError('Error: the number of primes to be returned must be non-negative.')
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
