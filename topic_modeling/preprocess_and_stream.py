import logging
import os
import sys
import re
import itertools

import nltk
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures

import gensim
from gensim.parsing.preprocessing import STOPWORDS

from utils.get_raw_reviews import get_list_of_raw_reviews

def init_logging():
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    logging.root.level = logging.INFO

def main():
    init_logging()
    
    print get_list_of_raw_reviews('../business_data/The\ Cellar\ Restaurant/')

if __name__ == "__main__": main()
