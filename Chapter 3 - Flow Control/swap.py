# Name:         swap.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  This exercise carries out some basic operations on variables.

"""
    This exercise carries out some basic operations on variables.
    Introduces learner to assignments, expressions, and types
"""


def get_valid_input(prompt):
    """
    Argument: prompt - The message displayed when prompting for a number.

    Functionality:  It takes in an input from the user
    and converts it to a string. Unless a valid number is provided, the user will
    be prompted to enter a new one.
    :return:
        Program returns a valid int number
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Try again.")


num1 = get_valid_input("Enter the first number: ")  # store the first number
num2 = get_valid_input("Enter the second number: ")  # store the second number
print("First number: ", num1)
print("Second number: ", num2)

# Check if the first number is odd
if num1 % 2 != 0:
    print("First number is odd. Switch numbers.")
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = abs(num1 - num2)
    print("NEW First number: ", num1)
    print("NEW Second number: ", num2)
else:
    print("First number is even. Do nothing.")  # Program does nothing if first number is even
