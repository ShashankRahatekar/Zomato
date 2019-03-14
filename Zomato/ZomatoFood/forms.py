from django import forms

class GetName(forms.Form):
	cityName = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', "id": "search", 'placeholder':"Search for Hotels around you"}))

class SearchHotelIn(forms.Form):
	SearchHotel = forms.CharField(max_length = 100)