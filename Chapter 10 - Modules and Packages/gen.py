#! /usr/bin/env python3
# Name:
# Author:
# Version:
# Description:

"""
    DocString:
"""

def frange(start, stop=None, step=0.25):
    if stop is None:
        stop = float(start)
        curr = 0.0
    else:
        current = float(start)

    while current < stop:
        yield current
        current += step


print(list(frange(1.1, 3)))
print(list(frange(1, 3, 0.33)))
print(list(frange(1, 3, 1)))
print(list(frange(3, 1)))
print(list(frange(1, 3, 0)))
print(list(frange(-1, -0.5, 0.1)))
