from pprint import pprint


def word_frequency(words):
    """
    Calculate the frequency and average length of words in a given list.

    Parameters:
    words (list): A list of strings representing words.

    Returns:
    dict: A dictionary with words as keys. Each key maps to another dictionary
    containing:
    - 'frequency': The number of occurrences of the word in the input list.
    - 'total_length': The total length of the word accumulated over all its occurrences.
    - 'average_length': The average length of the word.
    """
    word_dict = {}
    for word in words:

        if word in word_dict:
            word_dict[word]['frequency'] += 1
            word_dict[word]['total_length'] += len(word)
        else:
            word_dict[word] = {'frequency': 1, 'total_length': len(word)}

    for word in word_dict.keys():
        item = word_dict[word]
        item['average_length'] = item['total_length'] / item['frequency']

    pprint(word_dict)


fruits = ['apple', 'banana', 'orange', 'apple', 'apple']
word_frequency(fruits)
