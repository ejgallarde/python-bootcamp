#! /usr/bin/env python3
# Name:        counter_loops.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo different ways to write
#              a counter loop using while and for loops.
"""
    DocString:
"""

count = 0  # 1.Initialise counter.
while count < 10:  # 2.Test condition.
    print(count, end="\n")
    count += 1  # 3.Increment counter.

# Alternatively we could use a for loop plus the
# built-in range() function.
# range(start, stop, step)
for num in range(0, 10, 1):
    print(num)

# range(start, stop, step=1)
for num in range(0, 10):
    print(num)

# range(start=0, stop, step=1)
for num in range(10):
    print(num)
