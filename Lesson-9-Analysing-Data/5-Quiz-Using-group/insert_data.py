
#####  Code to insert data in database

import json


## Function to insert data
def insert_data(data,db):

	twitter = db.twitter
	twitter.insert_many(data)

	return


if __name__ == "__main__":

	from pymongo import MongoClient

	client = MongoClient("mongodb://localhost:27017")
	db = client.examples

	with open('twitter_org.json') as f:
		data = json.loads(f.read())
		insert_data(data,db)
		print(db.twitter.count())