#! /usr/bin/env python3
# Name:         .py
# Author:       Earl John Gallarde
# Revision:     v1.0
# Description:  This program will demo how to match str data using Regular Expressions
#               and the Python std library module re.py.
"""
    DocString:
"""
import re

# Open File Handle for READING in TEXT mode.
fh_in = open(r"words.txt", mode="rt")

# Iterate through file handle and read one line at a time
# using an ITERATOR for loop.
for line in fh_in:
    # Example of str testing.
    # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
    m = re.search(r"^the", line) # Match lines starting with 'the'.
    # m = re.search(r"ing$", line) # Match lines ending with 'ing'.
    # m = re.search(r"^.ing$", line) # Match lines with bing|ding|king....
    # m = re.search(r"^[pk]ing$", line) # Match lines with king|ping.
    # m = re.search(r"^...................$", line) # Match lines with exactly 19 chars.
    # m = re.search(r"^.{19}$", line) # Match lines with exactly 19 chars (same as above).
    # m = re.search(r"^[A-Z]", line) # Match lines starting with a capital.
    # m = re.search(r"[aeiou][aeiou][aeiou]", line) # Match lines with 3 consecutive vowels.
    # m = re.search(r"[aeiou]{5,}", line) # Match lines with at least 5 cons vowels.
    # m = re.search(r"[0-9][0-9]", line) # Match lines with a digit.
    # m = re.search(r"\.", line) # Match lines with a 'dot'.
    # m = re.search(r"^[A-Z].*[A-Z]$", line) # Match lines start/ending with a capital.
    # m = re.search(r"^[A-Z].{3}[A-Z]$", line) # Match lines of 5 chars start/ending with capital.
    # m = re.search(r"^(.)(.).\2\1$", line) # Match lines with 5 char palindromes.
    # m = re.search(r"^([A-Z]).*\1$", line, flags=re.IGNORECASE) # Match lines start/end with SAME capital.
    # m = re.match(r"^([A-Z]).*\1$", line)  # match() automatically looks for lines starting with pattern.
    # m = re.fullmatch(r"^([A-Z]).*\1$\n", line) # Match ENTIRE line (must explicitly include newline!
    if m:
        print(line, end="")


fh_in.close() # Flush buffers and close file handles.