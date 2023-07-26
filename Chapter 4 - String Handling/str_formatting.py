#! /usr/bin/env python3
# Name:        str_formatting.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo different ways of formatting strings using
# escape chars and concatenation, str justification methods, .format() method and
# f-strings.
"""
    DocString:
"""

# Planet info with distance to SUN in Giga-metres.
# This is a dictionary named planets (more of this in the next chapters)
# A dictionary is a key-value pair type of object
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
           }

print("Planets is of type", type(planets))

# Iterate through planet keys and display Planet info using
# escape chars and str concatenation. UGLY!
# keys() returns a set-like object of all the keys in the dictionary
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm " + str(hex(0xff)))

print("-" * 60)

# str justification methods and concatenation. OK!
# The rjust() method is a built-in function for string manipulation.
# This method returns a new string of a specified length ['width' - 1st parameter] after substituting the original
# string to the right, if necessary, and padding the left side with a specified character called
# ['fillchar' - 2nd parameter should be a single character string].

for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12, '.') + " Gm " + str(hex(0xff)).rjust(6))

print("-" * 60)

# str .format() method. GOOD!
# This is a string formatting expression which uses placeholders, denoted by the {} brackets
# Inside these placeholders, you can control the type and formatting of variables that are
# provided later in the format() method.
for planet in planets.keys():
    print("{0:>12s}: {1:.>12.3f} Gm {2:>#6x}".format(planet, planets[planet], 0xff))
# {0:>12s}: This is the first placeholder. The 0 indicates the position of the variable from the format() method.
# The :> is saying that we want the output to be right-aligned (that's what > specifies), and 12s specifies
# that the string (s) will take up 12 characters, padding with spaces as needed.

# 12.3f specifies that the floating point number (f) will have a width of 12 characters,
# with 3 places after the decimal.

# The :>#6x specifies that the output will be right-aligned, padded with ' ' if needed
# and 6x specifies that the number will be converted to hexadecimal (x) and will take up 6 spaces.
# '#' adds the 0x prefix for hexadecimal representation

print("-" * 60)

# Python 3.5 onwards - we have f-strings!  My Favourite!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.>12.3f} Gm {0xff:>#6x}")

print("-" * 60)

# Python 2 has an OLDER way of formatting strings. Don't use!
# Here for historical reasons - in case you see someone still using this!
for planet in planets.keys():
    print("%12s: %12.3f Gm %#6x" % (planet, planets[planet], 0xff))
