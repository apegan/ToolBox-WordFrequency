"""
Alisha Pegan
SoftDes Word Frequency Toolbox
Analyzes the word frequencies of words in The Jungle
"""

import string
from collections import Counter
with open('theJungle.txt', 'r') as f:
    lines = f.readlines()
f.close


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    curr_line = 0
    while file_name[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    HCstrip = file_name[curr_line+1:]
    lines = []
    for line in HCstrip:
        space = line.strip(' \n\t\r')
        punc = space.translate(str.maketrans('', '', string.punctuation))
        lowcase = punc.lower()
        lines.append(lowcase)
    words = [line.split(' ') for line in lines]
    word_list = []
    for line in words:
        for word in line:
            word_list.append(word)
    return word_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    wordfreq = Counter(word_list)
    return (n, wordfreq.most_common(n))


if __name__ == "__main__":
    f = get_word_list(lines)
    n, w = get_top_n_words(f, 10)
    print('The Top %s Words:' % (n,))
    for letter, count in w:
        print('%s: %d' % (letter, count))
