#! /usr/bin/env python3
# Name:         variables.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This exercise carries out some basic operations on variables.

"""
    This exercise carries out some basic operations on variables.
    Introduces learner to assignments, expressions, and types
"""

# Assume that we execute the following assignment statements:
width = 17
height = 12.0
delimiter = '.'
# For each of the following expressions,
# write the value of the expression and the type (of the value of the expression).

print(width / 2)  # 8.5
print(type(width / 2))  # float

print(width / 2.0)  # 8.5
print(type(width / 2.0))  # float

print(height / 3)  # 4.0
print(type(height / 3))  # float

print(1 + 2 * 5)  # 11
print(type(1 + 2 * 5))  # int

print(delimiter * 5)  # .....
print(type(delimiter * 5))  # string
