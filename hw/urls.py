# file: hw/urls.py

from django.urls import path
from django.conf import settings 
from . import views 

# URL patterns specific to hw app:
urlpatterns = [
    # path(r'', views.home, name="home"), # connects the empty string '' to views.home function in the views.py file
    path(r'', views.home_page, name="home_page"),
]