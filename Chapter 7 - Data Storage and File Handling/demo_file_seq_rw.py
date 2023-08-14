#! /usr/bin/env python3
# Name:        demo_file_seq_rw.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to Open and Close file
# handles for Sequential Reading, Writing and appending in Text mode.
"""
    DocString:
"""
import sys

movies = {'mahesh': ['rrr', 'avatar', 'avengers'],
          'craig': ['blues brothers', 'life of brian', 'jabberwocky'],
          'sajith': ['12 angry men', 'silence of lamb', 'shawshank redemption'],
          'shae': ['rent', 'gangster squad', 'chicago']
          }


# Open file handle for Writing in Text Mode.
# Replace the destination as needed
fh_out = open(r"movies.txt", mode="wt")

# Iterate through keys in the movies dict and write movie info
# to file handle using an ITERATOR for loop.
for name in movies.keys():
    print(f"{name}: {movies[name]}", end="\n", file=sys.stdout)
    print(f"{name}: {movies[name]}", end="\n", file=fh_out)
    # fh_out.write(f"{name}: {movies[name]}\n")
    # fh_out.writelines(['', '', '', '']) # Appends "\n" on each object in a list only!

fh_out.close()  # Flush buffers and close file handle.

print("-" * 60)

# Open file handle for READING in Text mode.
fh_in = open(r"movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str object. Be careful.
# text = fh_in.read(30) # Read NEXT 30 chars into str object.
# text = fh_in.readline() # Read NEXT line into str object.
# lines = fh_in.readlines() # Read ENTIRE lines into LIST object. Be Careful!
# print(lines[-1]) # Useful as you can index LIST to get specific lines.

# Iterate through file handle and read one line at a time.
# for line in open(r"C:\labs\projects\Oracle_Mar_2023\movies.txt", mode="rt"):
# Iterator for loop pus ITERATOR object (iter()/next())
for line in fh_in:
    print(line, end="")

# fh_in.flush() # Flush buffers.
fh_in.close()  # Close file handle.
