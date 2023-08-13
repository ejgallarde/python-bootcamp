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
