#! /usr/bin/env python3
# Name:         right_justify.py
# Author:       Earl John Gallarde
# Revision:     v1.0
# Description:  This program will teach the basics of writing a function.
"""
    Python provides a built-in function called len that returns the length of a string, so
    the value of len('allen') is 5.

    1. Write a function named right_justify that takes a string named s as a parameter and prints the
    string with enough leading spaces so that the last letter of the string is in
    column 70 of the display.

    2. A function object is a value you can assign to a variable or pass as an argument. For
    example, do_twice is a function that takes a function object as an argument and calls it twice:

    def do_twice(f):

    f()
    f()
    Here’s an example that uses do_twice to call a function named print_spam twice.
    def print_spam():
    print 'spam'
    do_twice(print_spam)

    a. Type this example into a script and test it.
    b. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
    function twice, passing the value as an argument.
    c. Write a more general version of print_spam, called print_twice, that takes a string as a
    parameter and prints it twice.
    d. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
    argument.
    e. Define a new function called do_four that takes a function object and a value and calls the
    function four times, passing the value as a parameter. There should be only two statements in
    the body of this function, not four.

"""


def right_justify(s):
    print(' ' * 69 + s)


def do_twice(f, s):
    f(s)
    f(s)


def do_four(f, s):
    do_twice(print_spam, s)
    do_twice(print_spam, s)


# Here’s an example that uses do_twice to call a function named print_spam twice.
def print_spam(spam):
    print(spam)


right_justify('EJ')
do_twice(print_spam, 'spam')
do_twice(right_justify, 'EJ')
do_four(do_twice, 'Caleb')


def print_diagram():
    i = 0
    while i < 3:
        print("+ " + "- " * 4 + "+ " + "- " * 4 + "+")
        if i == 2:
            break
        print_vertical()
        i += 1


def print_vertical():
    for i in range(3):
        print("|" + " " * 9 + "|" + " " * 9 + "|")


print_diagram()
