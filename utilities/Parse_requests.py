__author__ = 'Bryce Langlotz'

import sys
import json,httplib

allReviews = []
reviewsForRestaurant = []

def getBusinesses():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/Restaurants', '', {
       "X-Parse-Application-Id": "aS5JfOEzT7lLooye3NQCzkFQagbUXaQVhKX24wnE",
       "X-Parse-REST-API-Key": "N6SrV95BxIw970IsSLBYBdM4ik0dWFtTRhC3HYCx"
     })
    data = json.loads(connection.getresponse().read())
    return data["results"]

def getReviewsForBusiness(business):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('GET', '/1/classes/' + business, '', {
       "X-Parse-Application-Id": "aS5JfOEzT7lLooye3NQCzkFQagbUXaQVhKX24wnE",
       "X-Parse-REST-API-Key": "N6SrV95BxIw970IsSLBYBdM4ik0dWFtTRhC3HYCx"
     })
    data = json.loads(connection.getresponse().read())
    return data["results"]

def getAllReviews():
    reviewCollection = []
    restaurants = getBusinesses()
    for restaurant in restaurants:
        reviews = getReviewsForBusiness(restaurant["alpha_numeric_name"])
        reviewCollection += reviews
    return reviewCollection


if len(sys.argv) == 1:
    allReviews = getAllReviews()
    print(allReviews)
else:
    reviewsForRestaurant = getReviewsForBusiness(str(sys.argv[1]))
    print(reviewsForRestaurant)




