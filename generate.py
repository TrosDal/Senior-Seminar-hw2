#!/usr/bin/python

"""A Python program generating a list of prime numbers and output them into a csv file
"""

from primepackage import*

def main():
    """Generate 100 prime numbers and output it into output.csv file
    """
    primes = get_n_prime(100)

    write_primes(primes, 'output.csv')

    nums = read_primes('output.csv')

    print(nums)

if __name__ == '__main__':
    main()
