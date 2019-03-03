#collections.py

import requests
import json

def fetch_collections(city_id, api):
	collections_response = requests.get('https://developers.zomato.com/api/v2.1/collections?city_id='+city_id, headers={"user-key" : api, "Accept" : "application/json"})
	print(collections_response.status_code)

	collections_data = collections_response.json()

	for d in collections_data['collections']:
		print(str(d['collection']['collection_id'])+" "+d['collection']['title'])

api = '305821bf05bc53f67d7720d7f09eed61'

city_search = input('Enter City Name To Search: ')

city_code_response = requests.get('https://developers.zomato.com/api/v2.1/cities?q='+city_search, headers={"user-key" : api, "Accept": "application/json" })

data = city_code_response.json()

print(city_code_response.status_code)

city_ID=0

if (city_code_response.status_code!=200):
	print('Not A Valid API')
else:
	for d in data['location_suggestions']:
		city_ID = d['id']
		print(city_ID)

	fetch_collections(str(city_ID), api)

#https://developers.zomato.com/api/v2.1/collections?city_id=3 ->url for collections