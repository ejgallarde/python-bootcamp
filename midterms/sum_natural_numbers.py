#! /usr/bin/env python3
# Name:        sum_natural_numbers.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program calculates the sum of the first n natural numbers, skipping numbers that are multiples of m
def sum_natural_numbers(n, m):
    """
    Calculate the sum of the first n natural numbers, skipping numbers that are multiples of m.

    Parameters:
    - n (int): The number of natural numbers to sum up to.
    - m (int): The number to skip multiples of.

    Returns:
    - int: The sum of the first n natural numbers skipping multiples of m.
    - str: 'No output' if m is greater than or equal to n.
    """
    if m >= n:
        return "No output"
    sum_nat_num = 0
    for i in range(1, n + 1):
        if i % m != 0:
            sum_nat_num += n
    # total_sum = sum(i for i in range(1, n + 1) if i % m != 0)  - simpler
    return sum_nat_num


def sum_natural_numbers_ver2(n, m):
    """
    Calculate the sum of the first n natural numbers, skipping numbers that are multiples of m.

    Parameters:
    - n (int or str): The number of natural numbers to sum up to.
    - m (int or str): The number to skip multiples of.

    Returns:
    - int: The sum of the first n natural numbers skipping multiples of m.
    - str: 'No output' if m is greater than or equal to n.
    """
    try:
        m_int = int(m)
        n_int = int(n)
    except ValueError:
        # This block will execute if the conversion to integer fails
        return "Failed conversion to int. No output."

    if m >= n or n < 1:
        return "No output"
    sum_nat_num = 0
    for i in range(1, n + 1):
        if i % m != 0:
            sum_nat_num += n
    return sum_nat_num
