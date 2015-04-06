from __future__ import unicode_literals, print_function

import logging
import itertools
import pickle

import numpy as np
import gensim
from gensim.utils import smart_open, simple_preprocess
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki
from gensim.parsing.preprocessing import STOPWORDS

class ReviewCorpus(object):
    def __init__(self, raw_data, dictionary):
	self.raw_data_file = raw_data
	self.dictionary = dictionary
	for line in open(raw_data):
	    dictionary.doc2bow(line.lower().split(), allow_update=True)

    def __iter__(self):
	for line in open(self.raw_data_file):
	    yield self.dictionary.doc2bow(line.lower().split())

def init_logging():
    logging.basicConfig(format="%(levelname)s : %(message)s", level=logging.INFO)
    logging.root.level = logging.INFO

def head(stream, n=10):
    # Return first 'n' elements of stream as plain list
    return list(itertools.islice(stream, n))

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]

def main():
    init_logging()
    corpus = ReviewCorpus("./data/raw.txt", gensim.corpora.Dictionary())
    
    corpus.dictionary.save_as_text('data/review_dictionary.txt')
    gensim.corpora.MmCorpus.serialize('./data/review_dict.mm', corpus)

if __name__ == '__main__': main()
