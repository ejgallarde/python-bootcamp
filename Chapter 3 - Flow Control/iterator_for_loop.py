#! /usr/bin/env python3
# Name:        iterator_for_loop.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to ITERATE through
# collections (str/tuple/list/dict/sets) using an ITERATOR for loop.
"""
    DocString:
"""
#                0              1             2                 3                4               5
heroes = ['mother theresa', 'ghandi', 'william wallace', 'douglas bader', 'nelson mandela', 'donald duck']

# ITERATE through a collection using an ITERATOR for loop.
for name in heroes:
    print(name.title(), end="\n")

print("Heroes=", heroes)

# ITERATE through a collection AND modify the objects using an ITERATOR for loop.
idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1

print("Heroes=", heroes)

# ITERATE through a collection AND modify the objects using an ITERATOR for loop
# and built-in enumerate() function. Enumerate returns TUPLE (idx, next object).
for (idx, name) in enumerate(heroes, start=0):
    if isinstance(name, str):
        print(name.lower(), end="\n")
        heroes[idx] = name.lower()
    elif isinstance(name, float):
        heroes[idx] = name + 1.2

print("Heroes=", heroes)
