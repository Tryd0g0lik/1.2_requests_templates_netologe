from calculator.views import index, calc
from django.urls import path

urlpatterns=[
	path('', index, name='index'),
	path('result/', calc, name="result")
]
