#!/usr/bin/python
"""This module creates csv files of prime numbers,
and reads prime numbers from csv files."""

import csv

def write_primes(num_list, file_name):
    """Takes a list of prime numbers and writes them to a csv file."""
    with open(file_name, 'w', newline='') as p_file:
        file_writer = csv.writer(p_file)

        file_writer.writerow(num_list)

        p_file.close()

def read_primes(file_name):
    """Reads prime numbers from a csv file and places them into a list,
which it returns."""
    csv_file = open(file_name, 'r', newline='')
    file_read = csv.reader(csv_file)
    
    for num in file_read:
        return num
