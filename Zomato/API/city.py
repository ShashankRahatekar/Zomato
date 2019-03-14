import requests
api = '305821bf05bc53f67d7720d7f09eed61'
def LoadCity(name):
	
	q = name
	response = requests.get('https://developers.zomato.com/api/v2.1/cities?q='+q, headers={"user-key" : api, "Accept": "application/json" })

	data = response.json()

	if(response.status_code!=200):
		return ('Not Valid API')
	return data

def Collections_fetch(city_id):
	url = 'https://developers.zomato.com/api/v2.1/collections?city_id='
	Collections_response = requests.get(url+str(city_id), headers={"user-key" : api, "Accept": "application/json"})
	
	collections_data = Collections_response.json()
	print(collections_data)
	return collections_data

def Cusion_fetch(city_id):
	url = 'https://developers.zomato.com/api/v2.1/cuisines?city_id='

	Cusion_Response = requests.get(url+str(city_id), headers={"user-key" : api, "Accept" : "application/json"})

	Cusion_data = Cusion_Response.json()

	return Cusion_data

def Hotel_data(city_name):
	url = 'https://developers.zomato.com/api/v2.1/search?entity_type=city&q='

	Hotel_Response = requests.get(url+city_name, headers={"user-key" : api, "Accept":  "application/json"})
	print(url+city_name)
	Hotel_data_return = Hotel_Response.json()

	return Hotel_data_return

def Categories_List(request):
	url = 'https://developers.zomato.com/api/v2.1/categories'

	cat_return = requests.get(url, headers={"user-key" : api, "Accept": "application/json"})

	cat_data = cat_return.json()

	return cat_data