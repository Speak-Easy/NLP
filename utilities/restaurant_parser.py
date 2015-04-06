# This script separates reviews into directories corresponding to the
# business_id listed in the review

import json, os, errno, pickle
from shutil import copyfile

restaurants = pickle.load(open("restaurants.pickle", "rb"))

def make_directory(path, directory):
	if not os.path.exists(path + directory):
		os.makedirs(path + directory)

def get_restaurant_name(path, file_name):
	# opens a file as a JSON object
	obj = json.loads(open(os.path.join(path, file_name)).readline())
	return obj['name']

def open_json_object(path, f):
	return json.loads(open(os.path.join(path, f)).readline())

def main():
	restaurants_path = '../data_sets/restaurants/'
	reviews_path = '../data_sets/yelp_dataset/review'
	for key, item in restaurants.items():
		make_directory(restaurants_path, item)

	for root, _, files in os.walk(reviews_path):
	    for f in files:
	    	obj = open_json_object(reviews_path, f)
	    	business_id = obj['business_id']
	    	business_name = restaurants[business_id]
	    	copyfile(os.path.join(reviews_path, f), os.path.join(restaurants_path, business_name, f))

main()