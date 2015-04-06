from __future__ import division
from pattern.en import pluralize, singularize, suggest, ngrams, wordnet
import json, os, operator, pickle, re, sys, getopt, argparse


stopwords = ''
# using a global variable to count total number of words
total_count = 0

def open_pickle():
	global stopwords
	# open stopword list
	stopwords = pickle.load(open("stopwords/stopwords.pickle", "rb"))

def singularize_words(words_list):
	return map(singularize, words_list)

def lowercase_words(words_list):
	return map(lambda x: x.lower(), words_list)

def correct_words(words_list):
	return [tup[0][0] for tup in map(suggest, words_list)]

def word_in_stopwords(word):
	return word not in stopwords

def remove_stop_words(words_list):
	return filter(word_in_stopwords, words_list)

def correct_word(word):
	if word not in stopwords:
		return singularize(suggest(word.lower())[0][0])

def clean_words_list(words_list):
	return map(correct_word, words_list)

def calculate_percentage(word_dict, total):
	return {k: round(((v / total) * 100), 2) for k, v in word_dict.items()}

def generate_words(sentence, words):
	global total_count
	review_words = re.split('\W+', sentence)
	clean_words = clean_words_list(review_words)
	for word in clean_words:
		if word in words:
			words[word] += 1
		else:
			words[word] = 1
		total_count += 1
	return words

def generate_ngrams(sentence, ngrams_dict, n):
	global total_count
	for ngram in ngrams(sentence, int(float(n))):
		if ngram in ngrams_dict:
			ngrams_dict[ngram] += 1
		else:
			ngrams_dict[ngram] = 1
		total_count += 1
	return ngrams_dict


def generate_frequency(flag, review, frequencies):
	if flag is 'w':
		return generate_words(review, frequencies)
	elif is_number(flag):
		return generate_ngrams(review, frequencies, flag)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def execute(flag):
	directory = 'test_files'
	# create new dictionary
	frequencies = {}
	global total_count

	for root, _, files in os.walk(directory):
	    for f in files:
	        data = open('text_files/' + f)
	        # unncessary because its only one line
	        line = data.readline()
        	obj = json.loads(line)
        	if 'review_id' in obj:
        		review = obj['text']
    			generate_frequency(flag, review, frequencies)

	print(sorted(calculate_percentage(frequencies, total_count).items(), key=operator.itemgetter(1)))

# main accepts a flag that determines what frequency to calculate.
# If given a 'w', it will calculat word frequency. Any numeric flag
# will cause it to calculate frequencies of ngrams, where n is the
# value of the flag
def main(argv):
	parser = argparse.ArgumentParser(description='Generate a frequency table of ngrams')
	parser.add_argument('n', metavar = 'n', nargs = 1, help = 'determines value of n in ngram')
	args = parser.parse_args()
	d = vars(args)
	flag = d['n'][0]

	execute(flag)

if __name__ == "__main__": main(sys.argv[1:])
