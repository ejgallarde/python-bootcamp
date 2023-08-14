#! /usr/bin/env python3
# Name:        demo_sets.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to create, grow and shrink and combine
# sets. SETS = UNORDERED MUTABLE Collection of UNIQUE objects.
"""
    DocString:
"""

marvel_fans = {'shae', 'sai', 'saleem', 'sin guan', 'donald'}
dc_fans = set()  # Create Empty Set

dc_fans.add('manting')
dc_fans.add('mahesh')
dc_fans.add('donald')

# dc_fans.pop() # Randomly remove an object in set.
comic_fans = dc_fans.copy()  # Copy set.
comic_fans.clear()  # Empty Set.
comic_fans = set()  # Empty set (same as above.)

print(f"Marvel Fans = {marvel_fans}")
print(f"DC Fans = {dc_fans}")

print("-" * 60)

# Combine SETS using SET operators (Remember VENN diagrams).
print(f"Fans of BOTH Marvel OR DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of ONLY Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of EITHER Marvel OR DC= {marvel_fans.symmetric_difference(dc_fans)}")

print("-" * 60)
# Combine SETS using SET operators (Remember VENN diagrams).
print(f"Fans of BOTH Marvel OR DC = {marvel_fans | dc_fans}")
print(f"Fans of Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of ONLY Marvel = {marvel_fans - dc_fans}")
print(f"Fans of EITHER Marvel OR DC= {marvel_fans ^ dc_fans}")
