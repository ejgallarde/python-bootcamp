#! /usr/bin/env python3
# Name:        generator_functions.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to yield objects one at a time using
# a generator function (memory efficient).
"""
    DocString:
"""


def get_numbers():
    """ Return collection/list of numbers """
    print("Executing get_numbers()..")
    numbers = []
    for x in range(0, 1000000000000000):
        numbers.append(x)
    return numbers


def generate_numbers():
    """ Yield one collection object at a time (Lazy Collection) """
    print("Executing generate_numbers()..")
    for x in range(0, 10):
        yield x


# for z in get_numbers():
for z in generate_numbers():
    print(z)

# Alternatively we could use generator function with a while loop.
gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

# Alternatively we could use just manually request NEXT yielded value
gen = generate_numbers()
num1 = next(gen)
num2 = next(gen)
num3 = next(gen)
print(num1, num2, num3)
