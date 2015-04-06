# This script creates a pickle containing a dictionary mapping a
# business_id to a business name

import pickle, os, json

path = '../data_sets/yelp_dataset/restaurant'
file_directory = os.path.dirname(os.path.realpath(__file__))
restaurants = dict()

def add_to_map(dictionary, restaurant_name, restaurant_id):
	if not restaurant_id in dictionary:
		dictionary[restaurant_id] = restaurant_name

def open_json_object(f):
	return json.loads(open(os.path.join(path, f)).readline())

def pickle_dictionary(dictionary):
	with open(os.path.join(file_directory, 'restaurants.pickle'), 'wb') as pickled_restaurants:
		pickle.dump(dictionary, pickled_restaurants)

def main():
	for root, _, files in os.walk(path):
		for f in files:
			obj = open_json_object(f)
			add_to_map(restaurants, obj['name'], obj['business_id'])

	pickle_dictionary(restaurants)

main()
