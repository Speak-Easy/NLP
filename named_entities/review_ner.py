from __future__ import print_function

import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

sys.path.insert(0, os.path.abspath(os.path.join(os.curdir, os.pardir)))

from nltk.tag.stanford import NERTagger

from utilities.get_raw_reviews import clean_reviews

def init_ner_tagger():
    return NERTagger('./stanford_ner/english.all.3class.distsim.crf.ser.gz', './stanford_ner/stanford-ner.jar')

def get_reviews():
    parent_path = os.path.join(os.curdir, os.pardir)
    path = os.path.join(parent_path, 'business_data/La Fonda Latina')
    return map(lambda w: w.encode('ascii', 'ignore'), clean_reviews(path))

def write_named_entities_to_file(named_entities):
    with open("named_entites.txt", "w") as f:
	for word, tag in named_entities:
	    f.write("\t".join([word, tag, "\n"]))

def tag_reviews(reviews, tagger):
    return filter(lambda word_tag: word_tag[1] != 'O', tagger.tag(reviews))

def main():
    ner_tagger = init_ner_tagger()
    
    reviews = get_reviews()

    named_ents = tag_reviews(reviews, ner_tagger) 

    write_named_entities_to_file(named_ents)

if __name__ == "__main__": main()
