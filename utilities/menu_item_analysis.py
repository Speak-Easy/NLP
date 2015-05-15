#!/usr/bin/python
from __future__ import print_function, unicode_literals

import sys, os

import string

import nltk.data
from frequency import lowercase_words, singularize_words, correct_words, remove_stop_words
from get_raw_reviews import get_list_of_raw_reviews

pardir = os.path.join(os.curdir, os.pardir)
menu_path = os.path.join(pardir, 'menu.txt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

def clean_reviews(reviews):
    cleaned = map(string.split, reviews)

    cleaned = map(lowercase_words, cleaned)
    cleaned = map(remove_stop_words, cleaned)
    #cleaned = map(singularize_words, cleaned)

    cleaned = map(string.join, cleaned)

    return cleaned

def load_text_menu(menu_path):
    with open(menu_path) as f:
	return set(map(string.strip, f.read().split()))

def find_occurrences_of_menu_items(reviews, menu, tokenizer=tokenizer):

    for review in reviews:
	review_sentences = break_review_into_sentences(review)
	for sent in review_sentences:
	    
	    if (len(filter(lambda x: x in menu, sent.split())) > 0): 
		print('---', sent, '---', sep='\n')

def break_review_into_sentences(review, tokenizer=tokenizer):
    return tokenizer.tokenize(review)

def main(argv):
    docdir = argv[1] if len(argv) > 1 else os.curdir

    reviews = get_list_of_raw_reviews(docdir)

    reviews = clean_reviews(reviews)

    menu = load_text_menu(menu_path)

    find_occurrences_of_menu_items(reviews, menu)

if __name__ == "__main__": main(sys.argv)
