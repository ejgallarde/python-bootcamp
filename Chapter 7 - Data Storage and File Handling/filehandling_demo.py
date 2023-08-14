#! /usr/bin/env python3
# Name:        filehandling_demo.py
# Author:      Earl John Gallarde
# Revision:    v1.0
# Description: This program will demo how to open, close, read
# and write randomly to a file using the .seek() and .tell()

def demo():
    # create a new file
    f = open("myfile.txt", "w")
    string_to_write = "hello world"
    f.write(string_to_write)
    f.close()

    # read a file
    f = open("myfile.txt", "r")
    file_contents = f.read()
    print(file_contents)
    f.close()

    # append to a file
    f = open("myfile.txt", "a")
    string_to_write = "hello world\nwhat's up?"
    f.write(string_to_write)
    f.close()

    # read a file
    f = open("myfile.txt", "r")
    file_contents = f.read()
    print(file_contents)
    f.close()


def read_words(file_name):
    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    file_lines = file_contents.split("\n")
    word_count = 0
    for line in file_lines:
        line_list = line.split(" ")
        word_count += len(line_list)
    print(word_count)


def get_frequency(file_name):
    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    file_lines = file_contents.split("\n")
    dict_of_words = {}

    for line in file_lines:
        words = line.split(" ")
        for word in words:
            clean_word = word.lower()
            clean_word = clean_word.replace(",", "").replace(":", "").replace(".", "")
            if clean_word in dict_of_words.keys():
                dict_of_words[clean_word] += 1
            else:
                dict_of_words[clean_word] = 1
    sorted_dict = dict(sorted(dict_of_words.items(), key=lambda item: item[1]))
    print(sorted_dict)


def scramble_words(file_name):
    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
