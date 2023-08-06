#! /usr/bin/env python3
# Name:        file_random_rw.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to open, close, read
# and write randomly to a file using the .seek() and .tell()
"""
    DocString:
"""

SOF = 0  # Start of File.
CUR = 1  # Current position in file.
EOF = 2  # End of file.

# Open file handle for READING in TEXT mode.
with open(r"C:\labs\projects\Oracle_Mar_2023\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, SOF)  # Seek to char pos 90 from SOF.
    text = fh_in.read(30)
    print(f"Text at position {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(135, SOF)  # Seek to char pos 135 from SOF.
    text = fh_in.read(30)
    print(f"Text at position {fh_in.tell() - len(text)} = {text}")

# Open file handle for READING in BINARY mode.
with open(r"C:\labs\projects\Oracle_Mar_2023\movies.txt", mode="rb") as fh_in:
    fh_in.seek(-70, EOF)  # Seek back 70 bytes from EOF.
    text = fh_in.read(30)
    print(f"Text at position {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(-50, CUR)  # Seek back 50 bytes from current position.
    text = fh_in.read(30)
    print(f"Text at position {fh_in.tell() - len(text)} = {text}")
