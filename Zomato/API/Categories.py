import requests
import json
api = "305821bf05bc53f67d7720d7f09eed61"

response= requests.get('https://developers.zomato.com/api/v2.1/categories', headers={"user_key": api, "Accept": "application/json"})


data = response.json()

print(response.status_code)

for i in data['categories']:
	print(str(i['categories']['id'])+" "+str(i['categories']['name']))
