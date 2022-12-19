"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so. For the server extension, write your code in
extension_server.py
"""


def is_stopword(word, stopwords):
    """
    This function is passed:
        word: a string containing a word token

    The function returns a True value if given word is indeed a stopword, or False, if given word
    is not a stopword.

    >>> is_stopword('a', ['a', 'and'])
    True
    >>> is_stopword('nice', ['a', 'and'])
    False
    """

    return word in stopwords


def stem_word(word):
    """
    This function is passed:
        word: a string containing a word token

    The function returns stemmed version of giver word using Porter algorithm

    >>> stem_word('consulting')
    'consult'
    """

    from nltk.stem import PorterStemmer
    return PorterStemmer().stem(word)