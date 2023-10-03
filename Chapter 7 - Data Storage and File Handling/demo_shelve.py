#! /usr/bin/env python3
# Name:        .py
# Author:      Donald Cameron
# Revision:    v1.0
# Description: This program will demo how to PRESERVE multiple
# Python objects in one (database) file.
"""
    DocString:
"""

import shelve

movies = {'mahesh': ['rrr', 'avatar', 'avengers'],
          'craig': ['blues brothers', 'life of brian', 'jabberwocky'],
          'sajith': ['12 angry men', 'silence of lamb', 'shawshank redemption'],
          }

tv_shows = {'craig': ['goodies', 'thick of it'],
            'mahesh': ['suits', 'mandalorian']
            }

books = {'sajith': ['alchemist', 'hamlet'],
         'shae': ['culture vultures', 'the odyssey']
         }

with shelve.open(r"media") as db:
    db['films'] = movies
    db['tv'] = tv_shows
    db['books'] = books

with shelve.open(r"media") as db:
    print(f"Craig's favourite movies = {db['films']['craig']}")
    print(f"Shae's favourite book = {db['books']['shae'][0]}")
