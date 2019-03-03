from django import forms

class GetName(forms.Form):
	cityName = forms.CharField(max_length = 100)