#!/usr/bin/python
from __future__ import unicode_literals

import pickle, os
from nltk.corpus import stopwords
from pattern.en.wordlist import PROFANITY, STOPWORDS

file_directory = os.path.dirname(os.path.realpath(__file__))

def add_nltk_stopwords(stopword_set):
    map(stopword_set.add, stopwords.words('english'))

def add_mit_stopwords(stopword_set):
    with open(os.path.join(file_directory, 'english.stop')) as mit_stopwords_file:
        map(lambda x: stopword_set.add(x.strip()), mit_stopwords_file.readlines())

def add_additional_stopwords(stopword_set):
    with open(os.path.join(file_directory, 'english.stop')) as add_stopwords_file:
	map(lambda x: stopword_set.add(x.strip()), add_stopwords_file.readlines())

def add_pattern_stopwords(stopword_set):
    map(stopword_set.add, STOPWORDS)
    map(stopword_set.add, PROFANITY)

def pickle_stopwords(stopword_set):
    with open(os.path.join(file_directory, 'stopwords.pickle'), 'wb') as pickled_stopwords:
        pickle.dump(stopword_set, pickled_stopwords)

def main():
    set_of_stopwords = set()
    add_nltk_stopwords(set_of_stopwords)
    add_mit_stopwords(set_of_stopwords)
    add_additional_stopwords(set_of_stopwords)
    add_pattern_stopwords(set_of_stopwords)
    pickle_stopwords(set_of_stopwords)

if __name__ == "__main__": main()
