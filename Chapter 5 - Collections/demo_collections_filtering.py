#! /usr/bin/env python3
# Name:        collections_filtering.py
# Author:      Earl John Gallarde
# Version :    v1.0
# Description: This program will demo different ways to Copy Collections to a new collection
# with optional filtering - using for loops + if, lambda functions, and comprehensions!
"""
    DocString:
"""

# Source collection (list of names).
students = ['sai', 'earl', 'sajith', 'guangyu', 'manting', 'craig', 'shae', 'mahesh', 'shae']

# Copy and filter source collection to a dest collection using..
# 1.Iterator for loop plus source, option if condition (filtering), expression.
wee_names = []
for name in students:  # 1.Iterator loop plus source.
    if len(name) <= 5:  # 2.Optional condition (filtering).
        wee_names.append(name.upper())  # 3. Expression (do anything with data?).

print(f"1.Short names = {wee_names}")


def filter_names(name):
    """ Return True if name is less than 5 chars """
    if len(name) <= 5:
        return True
    else:
        return False


# 2.Iterator for loop plus source, user function (filtering), expression.
wee_names = []
for name in students:  # 1.Iterator loop plus source.
    if filter_names(name):  # 2.Optional condition (filtering).
        wee_names.append(name.upper())  # 3. Expression (do anything with data?).

print(f"2.Short names = {wee_names}")

# 3.Built-in filter() function (iteration), user function (filtering). NO EXPRESSION! :-(
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4.Built-in filter() function (iteration), lambda function (filtering). NO EXPRESSION! :-(
wee_names = list(filter(lambda name: len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5.List Comprehension - expression, iterator loop plus source, optional condition.
wee_names = [name.upper() for name in students if len(name) <= 5]
print(f"5.Short names = {wee_names}")

# 5.1 List Comprehension - expression, iterator loop plus source, optional condition.
wee_names = [(name.upper(), len(name)) for name in students if len(name) <= 5]
print(f"5.1.Short names = {wee_names}")

# 5.2 DICT Comprehension - expression, iterator loop plus source, optional condition.
# Dict = UNIQUE Keys = Extra filtering!!!
wee_names = {name.upper(): len(name) for name in students if len(name) <= 5}
print(f"5.2.Short names = {wee_names}")

# 5.3 SET Comprehension - expression, iterator loop plus source, optional condition.
# Dict = UNIQUE Values = Extra filtering!!!
wee_names = {name.upper() for name in students if len(name) <= 5}
print(f"5.3.Short names = {wee_names}")
