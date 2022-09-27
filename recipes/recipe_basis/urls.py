from django.urls import path
from urllib import request
from .views import *
from .views import recipe
urlpatterns = [
	# адреса приложения 'recipe_basis'
	path('', recipe(request) ),
	path('', menuMain, name='index')
]