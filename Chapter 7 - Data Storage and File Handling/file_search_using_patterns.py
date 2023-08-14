#! /usr/bin/env python3
# Name:        file_search_using_patterns.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will define a reusable user function for matching regex
# patterns against lines in a file/s.
"""
    DocString:
"""
import re
import sys


# Example of a user function with parameter passing, default
# values and annotations.
def count_pattern_match(pattern: str = r"^.{19}$", file: str = r"words.txt") -> int:
    lines = 0
    with open(file, mode="rt") as fh_in:
        for line in fh_in:
            m = re.search(pattern, line, flags=re.IGNORECASE)
            if m:
                print(line, end="")
                lines += 1

    return lines


def main():
    count_pattern_match(r"^.{19}$", r"words.txt")
    return None


if __name__ == "__main__":
    import cProfile

    cProfile.run("main()")
    # main()
    sys.exit(0)
