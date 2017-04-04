"""
Alisha Pegan
SoftDes Word Frequency Toolbox
Analyzes the word frequencies of words in The Jungle
"""

import string
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
    WPstrip = [line.strip(' \n\t\r') for line in HCstrip]
    PuncStrip = [s.translate(str.maketrans('', '', string.punctuation))
                 for s in WPstrip]
    lowcase = [text.lower() for text in PuncStrip]
    word_list = [line.split(' ') for line in lowcase]
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
    pass


if __name__ == "__main__":
    f = get_word_list(lines)
    print(f)
