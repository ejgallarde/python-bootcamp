#! /usr/bin/env python3
# Name:        str_split_join.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to split and re-join
# strings using the .split() and .join() methods.
"""
    DocString:
"""

# Sample line from /etc/passwd on Linux for the root user.
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# I want to modify some fields in the string line.
# BUT str objects are IMMUTABLE/READ ONLY!

fields = line.split(":")  # Returns a LIST (MUTABLE/Read Write).
fields[4] = "The Administrator"
fields[6] = "/bin/bash"

line = ":".join(fields)  # Returns a str.
print(line)