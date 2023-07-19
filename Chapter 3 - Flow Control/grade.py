#! /usr/bin/env python3
# Name:         grade.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This exercise focuses on flow control using the if-elif-else statement.

"""
    This exercise carries out some basic operations on variables.
    This exercise also carries out some basic if-elif-else statements.
"""

grade = int(input("Enter an int from 0-100:"))  # Assume correct input

# if-elif-else statement for identifying grade in letter
if grade > 89:
    letter_grade = 'A'
elif grade > 79:
    letter_grade = 'B'
elif grade > 69:
    letter_grade = 'C'
else:
    letter_grade = 'F'

print(letter_grade)

# Switch 2 numbers
num1 = int(input("Enter first number: "))  # Assume correct input
num2 = int(input("Enter second number: "))  # Assume correct input
print("First number: ", num1)
print("Second number: ", num2)

if num1 % 2 != 0:
    print("First number is odd. Switch numbers.")
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = abs(num1 - num2)
    print("NEW First number: ", num1)
    print("NEW Second number: ", num2)
else:
    print("First number is even. Do nothing.")
