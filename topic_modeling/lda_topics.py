## Gets the topics in the corpus using Latent Dirchlet Allocation (LDA)
from __future__ import print_function

import logging, gensim, bz2
import argparse, sys

from gensim import corpora, models, similarities

corpus = ''
dictionary = ''

def run_LDA():
    print('lda')
    global corpus, dictionary
    # extract 100 LDA topics, using 1 pass and updating once every 1 chunk (10,000 documents)
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=100, update_every=1, chunksize=10000, passes=1)

    # print the most contributing words for 20 randomly selected topics
    print(lda)
    
    print(lda.show_topics(20))

def run_LSI():
    print('lsi')
    global corpus, dictionary
    print(corpus)
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=20)
    print(lsi.show_topics(10))

def run_model(model):
    global corpus, dictionary
    # load corpus iterator
    corpus = gensim.corpora.MmCorpus('data/review_dict.mm')
    
    # load dictionary
    dictionary = gensim.corpora.Dictionary.load_from_text('data/review_dictionary.txt') 

    if (model == 'lda'):
        run_LDA()
    elif (model == 'lsi'):
        run_LSI()

# takes in a command line argument determining which kind of model to run
def main(argv):
    parser = argparse.ArgumentParser(description='Perform topic modeling of corpus')
    parser.add_argument('model', metavar = 'model', nargs = 1, help = 'specify model to use')
    args = parser.parse_args()
    d = vars(args)
    model = d['model'][0]

    run_model(model)

if __name__ == "__main__": main(sys.argv[1:])
