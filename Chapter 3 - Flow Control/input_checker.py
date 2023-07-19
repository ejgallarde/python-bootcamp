#! /usr/bin/env python3
# Name:         input_checker.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This exercise focuses on flow control and the input().

"""
    This exercise carries out some basic operations on flow control
"""


def get_valid_int_input():
    while True:
        try:
            return int(input("Enter an int: "))
        except ValueError:
            print("Try again.")


myInt = get_valid_int_input()
print(myInt)
