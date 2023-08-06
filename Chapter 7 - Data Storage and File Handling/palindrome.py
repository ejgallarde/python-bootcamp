# Name:        palindrome.py
# Author:      Earl John Gallarde
# Revision:    v1.0

"""
1. Understanding the Problem: The first step in this exercise is to understand the problem. You are required to write a
Python program that checks if the content of a text file is a palindrome. A palindrome is a word, phrase, number, or
other sequence of characters that reads the same forward & backward (ignoring spaces, punctuation, and capitalization).

2. Reading from a File: Learn how to read the content of a text file in Python. Use the open() function with the 'r'
mode. Use the read() method to read the content of the file.

3. Checking for Palindrome: Write a function that checks if a string is a palindrome. The function should ignore spaces,
 punctuation, and capitalization.

4. Writing to a File: If the content of the file is not a palindrome, you should reverse the string and write it to a
new file. The new file should have the same name as the original file but with a suffix of '_reversed.txt'. Use the
open() function with the 'w' mode to write to a file.

5. Using Docstrings: Remember to include docstrings in your functions to explain what they do. Docstrings are a type of
comment that appear at the beginning of a function and are used to explain the purpose of the function.
"""
import re  # importing the re library to help with regular expressions


def read_file(filename):
    """
    Read the content of a file.

    Parameters:
    filename (str): The name of the file to read.

    Returns:
    str: The content of the file.
    """
    with open(filename, 'r') as file:
        content = file.read()
    return content


def is_palindrome(text):
    """
    Check if a given string is a palindrome.

    Parameters:
    text (str): The text to check.

    Returns:
    bool: True if the text is a palindrome, False otherwise.
    """
    # Remove all non-alphabetic characters and convert to lowercase
    # sub function is used to replace parts of a string that match a particular pattern
    # the sub function takes in the regu
    text = re.sub('[^a-z]', '', text.lower())  # replace anything that is not a lower case alphabet with empty string

    print(f"After word cleansing, text is: {text}")
    # Check if the text is the same when reversed
    return text == text[::-1]


def write_to_file(filename, content):
    """
    Write a string to a file.

    Parameters:
    filename (str): The name of the file to write to.
    content (str): The content to write to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)


def process_file(filename):
    """
    Process a file to check if its content is a palindrome.
    If it's not a palindrome, write the reversed content to a new file.

    Parameters:
    filename (str): The name of the file to process.
    """
    # Read the content of the file
    content = read_file(filename)

    # Check if the content is a palindrome
    if not is_palindrome(content):
        print('The word is NOT a palindrome')
        # Since it's not a palindrome, reverse the content
        reversed_content = content[::-1]

        # Write the reversed content to a new file
        reversed_filename = filename.split('.')[0] + '_reversed.txt'
        write_to_file(reversed_filename, reversed_content)
    else:
        print('The word is a palindrome')


def main():
    print("Processing input.txt")
    process_file('input.txt')

    print("Processing input2.txt")
    process_file('input2.txt')


if __name__ == "__main__":
    main()
