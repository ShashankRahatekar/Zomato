from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
from django.shortcuts import render
from django import template
from django.template.loader import get_template

from API.city import LoadCity, Collections_fetch, Cusion_fetch, Hotel_data, Categories_List

from ZomatoFood.forms import GetName
# Create your models here.
#Get city code of Zomato City
def cities(request, name):
	city_data = LoadCity(name)
	id = 0
	for d in city_data['location_suggestions']:
		id = d['id']
	context = collections_List(request, id, name)
	
	return context

def search_Page(request):
	if request.method == 'POST':
		myform = GetName(request.POST)
		if myform.is_valid():
			name = myform.cleaned_data['cityName']
			cont = cities(request, name)
			#cities(request, name)
			temp = get_template('city_name.html')
			return HttpResponse(temp.render(cont, request))
	else:
		#Display Some Hotels of Pune In Home Page
		#Calling Colections API of Zomato
		Collection_data = Collections_fetch(5)
		tempData = []
		data = []

		for i in Collection_data['collections']:
			title = i['collection']['title']
			img_url = i['collection']['image_url']
			desc = i['collection']['description']
			href = i['collection']['url']
			tempData.append([title, img_url, desc, href])

		for i in range(6):
			data.append(tempData[i])
		form = GetName()
		context = {
			"form" : GetName(),
			"data" : data
		}
		
		return render(request, 'city_search.html', context);

def collections_List(request, city, city_name):
	collections_data = Collections_fetch(city)
	data = []
	for d in collections_data['collections']:
		collect_id = d['collection']['collection_id']
		res_count = d['collection']['res_count'] 
		img_url = d['collection']['image_url'] 
		title = d['collection']['title']
		share_url = d['collection']['share_url']
		data.append([collect_id, res_count, img_url, title, share_url])
	
	cuisine_data = Cusion_search(request, city)
	cuisine_data.sort()
	
	#Queue All Hotels of City

	hotels_list = Hotel_List(request, city_name)

	context = {
		"data" : data,
		"cusion_data" : cuisine_data,
		"total_cuision" : len(cuisine_data),
		"hotels_list" : hotels_list,
	}
	return context

def Cusion_search(request, city):
	Cusion_data = Cusion_fetch(city)

	data = []

	for d in Cusion_data['cuisines']:
		cuisine_id = d['cuisine']['cuisine_id']
		cuisine_name = d['cuisine']['cuisine_name']
		data.append([cuisine_id, cuisine_name])
	
	return data

#List all hotel Hotel_List
def Hotel_List(request, city):
	Hotel_data_list = Hotel_data(city)
	data = []

	for d in Hotel_data_list['restaurants']:
		hotel_id = d['restaurant']['id']
		hotel_name = d['restaurant']['name']
		hotel_addr = d['restaurant']['location']['address']
		hotel_local = d['restaurant']['location']['locality']
		hotel_city = d['restaurant']['location']['city']

		data.append([hotel_id, hotel_name, hotel_addr, hotel_local, hotel_city])

	return data
#Returns Categories_List Form and Result
def collection_List(request):
	print('Inside collection_List')			
	coll_data = Categories_List(request)
	data = []

	for d in coll_data['categories']:
		data.append([d['categories']['id'], d['categories']['name']])
	cont = {
		"data" : data
	}
	temp = get_template('categories_Result.html')
	return HttpResponse(temp.render(cont, request))