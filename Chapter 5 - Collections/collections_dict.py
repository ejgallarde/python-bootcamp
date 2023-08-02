#! /usr/bin/env python3
# Name:        collections_dict.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to define, grow and shrink a dict
# and access the keys and objects within.
"""
    DocString:
"""
import pprint

# Create a multidimensional dict of lists.
movies = {'mahesh': ['rrr', 'avatar', 'avengers'],
          'craig': ['blues brothers', 'life of brian', 'jabberwocky'],
          'sajith': ['12 angry men', 'silence of lamb', 'shawshank redemption'],
          'shae': ['rent', 'gangster squad', 'chicago']}

print(f"Mahesh's ALL favourite movies = {movies.get('mahesh')}")
print(f"Mahesh's ALL favourite movies = {movies['mahesh']}")
print(f"Mahesh's REAL favourite movies = {movies['mahesh'][0]}")

print("-" * 60)
movies.pop('craig')  # Remove key+object from dict.
# movies.pop('donald') # Return ERROR if key does not exist!
# movies.popitem() # Remove last key+object inserted.

films = movies.copy()  # Copy dict.
films.clear()  # Empty dict.
pprint.pprint(films)  # films have been cleared. displays an empty dict

print("-" * 60)

pprint.pprint(movies)
print("End of second pprint")
print("-" * 60)
# ITERATE through the dict keys using an ITERATOR for loop.
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

# ITERATE through the dict values using an ITERATOR for loop.
for films in movies.values():
    print(f"{films}")

print("-" * 60)
# ITERATE through the dict keys+values using an ITERATOR for loop.
# Returns TUPLE (key, value)
for (name, films) in movies.items():
    print(f"{name} LOVES {films}")
