import requests
import json
with open('API.json') as file:
	API_Data = json.load(file)

#print(API_Data)
api = ''
for d in API_Data['api']:
	if(d['name'] == 'MapQuest'):
		api= d['api']

print(api)
url = 'http://www.mapquestapi.com/geocoding/v1/address?key='+ api +'&location='
nom = requests.get(url+'Pune')

data = nom.json()

lat , lng = '', ''

for d in data['results']:
	for x in d['locations']:
		lat = x['latLng']['lat']
		lng = x['latLng']['lng']

print(str(lat)+" "+str(lng))
