#! /usr/bin/env python3
# Name:        sum_natural_numbers.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program checks if a number is prime


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6
    return True


def count_prime_words(filename):
    """
    Count the number of words in the file that have a prime number of letters.

    Args:
    - filename (str): Path to the file.

    Returns:
    - int: Number of words with a prime number of letters.
    - None: If the file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            words_with_prime = 0
            for line in file.readlines():
                words = line.split('')
                for word in words:
                    if is_prime(len(word)):
                        words_with_prime += 1
        return words_with_prime
    except FileNotFoundError:
        return None
