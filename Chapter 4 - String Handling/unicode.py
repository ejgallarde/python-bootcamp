#! /usr/bin/env python3
# Name:        unicode.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will display the entire Unicode char set from
# position 0 -> 65535 using an ITERATOR for loop plus the built-in range() function.
"""
    DocString:
"""

for pos in range(0, 65536, 1):
    try:
        print(chr(pos), end=" ")
        if pos % 16 == 0:  # add a line break after every 16 characters
            print("\n")
    except UnicodeEncodeError:
        print(" ")
