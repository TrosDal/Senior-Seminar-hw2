#!/usr/bin/python
"""This module creates csv files of prime numbers,
and reads prime numbers from csv files.

This module contains the functions "write_primes",
which writes a list of prime numbers to a file,
and "read_primes" which reads numbers from a csv file
and places them into a list.
"""

__author__ = "Rene Zambrana"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "rxzambrana@valdosta.edu"
__status__ = "Prototype"

import csv

def write_primes(num_list, file_name):
    """Takes a list of prime numbers and writes them to a csv file.

    The write_primes function accepts a list of prime numbers and a
    file name and writes the primes to a file with the given name.

    Args:
        num_list (int): list integers to be written to file.
        file_name (str): desired name of the output file.

    Returns:
        void: it creates an output file, but does not return anything.

    Raises:
        inputMismatchException: When an incorrect value is supplied.
        IOError: io error for when a file can't be opened/created.

    Examples:
        >>>> write_primes(prime_list, "primes.csv");
        >>>> write_primes([2,3,5,7,11], "primes.csv");
    """
    with open(file_name, 'w', newline='') as p_file:
        file_writer = csv.writer(p_file)

        file_writer.writerow(num_list)

        p_file.close()

def read_primes(file_name):
    """Reads prime numbers from a csv file and places them into a list,
    which it returns.

    The read_primes function accepts a file name and
    returns a list of the integers found in that file.

    Args:
        file_name (str): name of the input file.

    Returns:
        list (int): Returns a list of numbers read from the file.

    Raises:
        inputMismatchException: When an incorrect value is supplied.
        IOError: io error for when a file can't be opened/created.

    Examples:
        >>>> read_primes("primes.csv");
    """
    csv_file = open(file_name, 'r', newline='')
    file_read = csv.reader(csv_file)
    
    for num in file_read:
        return num
