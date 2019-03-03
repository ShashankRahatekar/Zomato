from django.urls import path
from . import views
from ZomatoFood.views import cities,search_Page, Cusion_search
from django.conf.urls import url
urlpatterns = [
    url(r'$', search_Page),
]