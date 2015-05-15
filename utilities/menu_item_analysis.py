#!/usr/bin/python
from __future__ import print_function, unicode_literals

import sys, os

import string
from collections import Counter

import nltk.data
from frequency import lowercase_words, singularize_words, open_pickle
from get_raw_reviews import get_list_of_raw_reviews

pardir = os.path.join(os.curdir, os.pardir)
menu_path = os.path.join(pardir, 'menu.txt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
stopword_path = os.path.dirname(os.path.realpath(__file__))
stopword_path = os.path.join(stopword_path, 'stopwords/stopwords.pickle')

def clean_reviews(reviews, stopwords):
    cleaned = map(string.split, reviews)

    cleaned = map(lowercase_words, cleaned)
    #cleaned = [filter(lambda x: x not in stopwords, review) for review in cleaned]
    #cleaned = map(singularize_words, cleaned)

    cleaned = map(string.join, cleaned)

    return cleaned

def load_text_menu(menu_path):
    with open(menu_path) as f:
	return set(map(string.strip, f.read().split()))

def find_occurrences_of_menu_items(reviews, menu, tokenizer=tokenizer):

    word_counts = Counter()

    for review in reviews:
	review_sentences = break_review_into_sentences(review)
	for sent in review_sentences:
	    
	    if (len(filter(lambda x: x in menu, sent.split())) > 0): 
		print('---', sent, '---', sep='\n')
		word_counts.update(sent.split())
		

    return word_counts
		

def break_review_into_sentences(review, tokenizer=tokenizer):
    return tokenizer.tokenize(review)

def main(argv):

    stopwords = open_pickle(stopword_path)

    docdir = argv[1] if len(argv) > 1 else os.curdir

    reviews = get_list_of_raw_reviews(docdir)

    reviews = clean_reviews(reviews, stopwords)

    menu = load_text_menu(menu_path)

    word_counts = find_occurrences_of_menu_items(reviews, menu)

    print('\n\n\n', word_counts.most_common(20))

if __name__ == "__main__": main(sys.argv)
