#! /usr/bin/env python3
# Program Name: average.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This exercise carries out some basic operations on variables.

"""
This program takes three integers as input from the user: num1, num2, and num 3.
The program should then perform the ff operations:

1.Calculate the average of the three numbers and store it in a variable called average.
2.Determine and store the maximum of the three numbers in a variable called maximum.
3.Determine and store the minimum of the three numbers in a variable called minimum.
4.Calculate the sum of the squares of num1, num2, and num3, and store the result in a variable called sum_of_squares.
5.Finally, display the calculated average, maximum, minimum, and sum_of_squares values to the user.

Considerations:

Use appropriate variables (follow proper variable naming convention) to store intermediate results, if you make use of any intermediate variables.

You will be using appropriate expressions, statements, and control flow structures (IF-THEN statements).
"""
import sys

# Function to validate input as integer
def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Take input from user:
num1 = validate_input("Enter first number:")
num2 = validate_input("Enter second number:")
num3 = validate_input("Enter third number:")

# Get the average of the 3 values
average = (num1 + num2 + num3) / 3
print("Average:", average)

# Get the maximum of the 3 values
maximum = max(num1, num2, num3)
print("Maximum:", maximum)

# Get the minimum of the 3 values
minimum = min(num1, num2, num3)
print("Minimum:", minimum)

# Get the sum of squares of the 3 values
sum_of_squares = num1 ** 2 + num2 ** 2 + num3 ** 2
print("Sum of squares:", sum_of_squares)

sys.exit(0)