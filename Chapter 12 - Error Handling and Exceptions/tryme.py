import numpy as np

print(np.empty(2))


try:
    with open(r"words2.txt", mode='rt') as file:
        words = [line.strip() for line in file]
        print(words)
except FileNotFoundError:
    print("File not found")

try:
    with open(r"words2.txt", mode='rt') as file:
        words = file.readlines()
        print(words)
        for word in words:
            print(word, end='')
        print("********************************")
except FileNotFoundError:
    print("File not found")

try:
    with open(r"words2.txt", mode='rt') as file:
        words = file.read()
        print(words)
        for word in words:
            print(word)
except FileNotFoundError:
    print("File not found")

