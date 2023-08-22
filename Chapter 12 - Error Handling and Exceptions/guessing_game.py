# Name: StrikeoutError
# Author: Earl John Gallarde LT9
# Version: 1.0
# Description: This code demonstrates the custom exception StrikeoutError
"""
Program Flow:
1. A random word is chosen from words.txt. Clues will be provided for the random word.
2. Player is given 5 chances to guess all the letters in the random word. (MAX_GUESSES = 5)
3. For each correct guess, the letter will be added to the guessed_letter list. Game status is then printed.
4. For each incorrect guess, the letter will be added to the incorrect_guesses list. Game status is then printed.
5. Player wins if he guesses all the letters in the random word.
6. StrikeoutError is raised when player maxes out the allowed number of guesses.
"""

import random


class StrikeoutError(Exception):
    """
    In a word-guessing game, the StrikeoutError is raised when the player makes n wrong guesses
       max_strikes (int) - number of allowed wrong guesses
       word (str) - the correct word in the guessing game
    """
    def __init__(self, max_strikes, word, message=None):
        self.max_strikes = max_strikes
        self.word = word
        if message is None:
            message = f"Player has reached {max_strikes} incorrect guesses. The word was '{word}'."
        super().__init__(message)


def guess_a_letter():
    letter = input("Enter a single letter: ")
    return letter.upper()


def print_game_status(guessed_letters, incorrect_guesses, word_to_guess):
    print(f"\nCorrect guesses: {guessed_letters}")
    print(f"Incorrect guesses ({len(incorrect_guesses)}): {incorrect_guesses}")
    if set(guessed_letters) == set(word_to_guess):
        print("You have guessed all the letters in the word.")
        print(f"The word is: {word_to_guess}")
        exit()


def play_guessing_game(word_to_guess):
    MAX_GUESSES = 5
    print("\nGuess the MAGIC word. You have 5 tries. No penalties for correct guesses.")
    print("CLUES:")
    print(f"  The word to guess has {len(word_to_guess)} letters.")
    unique_letters = set(word_to_guess)
    print(f"  The word to guess has {len(unique_letters)} unique letters.\n")

    guessed_letters = []
    incorrect_guesses = []
    while len(incorrect_guesses) < MAX_GUESSES:
        guessed_letter = guess_a_letter()
        if guessed_letter in word_to_guess and guessed_letter not in guessed_letters:
            guessed_letters.append(guessed_letter)
        elif guessed_letter not in word_to_guess and guessed_letter not in incorrect_guesses:
            incorrect_guesses.append(guessed_letter)
        print_game_status(guessed_letters, incorrect_guesses, word_to_guess)

    raise StrikeoutError(MAX_GUESSES, word_to_guess)


try:
    with open(r"words.txt", mode='rt') as file:
        words = [line.strip() for line in file]
        filtered_words = [word.upper() for word in words if word.isalpha() and len(word) < 8]
        random_word = random.choice(filtered_words)
        assert random_word.isalpha() and len(random_word) < 8, f"Invalid word selected: {random_word}"
        play_guessing_game(random_word)
except FileNotFoundError:
    print(f"File does not exist.")
except StrikeoutError as e:
    print("\n5 STRIKES, you're out!")
    print(e)  # This will print the message set in the StrikeoutError exception.
