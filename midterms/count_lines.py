#! /usr/bin/env python3
# Name:        count_lines.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program counts the number of lines in a file


def count_lines(filename):
    """
    Count the number of lines in a file.

    Args:
    - filename (str): Path to the file.

    Returns:
    - int: Number of lines in the file if the file exists.
    - None: If the file does not exist.

    Example:
    sample.txt contents:

    Hello, world!
    Python is an interesting language.
    End of file.

    This should output 3
    """
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return None


print(count_lines("sample.txt"))
