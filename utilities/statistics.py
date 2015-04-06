from __future__ import unicode_literals

import pattern, json, os, pickle, re

import matplotlib.pyplot as plt
from pattern.en import singularize, suggest
from frequency import singularize_words, lowercase_words, correct_words

file_dir = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(file_dir, 'sentiment_files/positive.txt')) as f:
    positives = set([line.strip() for line in f.readlines()])

with open(os.path.join(file_dir, 'sentiment_files/negative.txt')) as f:
    negatives = set([line.strip() for line in f.readlines()])

def autopct_func(pct):
    total = number_of_positive_words + number_of_negative_words
    val = int(pct*total/100.0)
    return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

def count_positives_and_negatives(review_text):
    words = re.split('\W+', review_text)
    words = correct_words(lowercase_words(singularize_words(words)))
    
    num_pos = 0
    num_neg = 0
    for word in words:
	if word in positives: num_pos += 1
	if word in negatives: num_neg += 1
	
    return num_pos, num_neg

def main():
    global number_of_positive_words
    global number_of_negative_words
    number_of_positive_words = 0
    number_of_negative_words = 0

    for root, _, files in os.walk('test_files'):
	for f in files:
	    with open(os.path.join('text_files', f)) as next_file:
		jsondata = json.loads(next_file.readline())
	    
	    if 'review_id' in jsondata:
		review_text = jsondata['text']
		new_pos, new_neg = count_positives_and_negatives(review_text)
		number_of_positive_words += new_pos
		number_of_negative_words += new_neg

    plt.pie([number_of_positive_words, number_of_negative_words], colors=('g', 'r'), labels=['Positive Words', 'Negative Words'], autopct=autopct_func)
    plt.show()

if __name__ == "__main__": main()
