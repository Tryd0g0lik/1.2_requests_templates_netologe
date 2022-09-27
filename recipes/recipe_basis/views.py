import html
from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from recipe_basis.module.menu import Menu
from recipe_basis.module.basis_recipe import Basis
import json
from urllib import request
from django.template import loader
# Create your views here.

def menuMain(request):

	fileName = "data.json"
	"""
	Returns a first element is a file name, the second element command's  the symbol for run a menu
	:param fileName: The file name there has recipes list
	:return:
	"""
	obj_menu = Menu()
	menu = obj_menu.menu(fileName)

	main_menu = f"""
Меню команды для выбора рецепта:; {menu[0]}
""".split(";")
	return render(request=request, template_name='recipe_basis/index.html', context={'text' : main_menu})


def omlet(request):
	# current_name = forms.CharField(label='Your name', max_length=100)
	comr = request.POST.get('command')
	if comr == 'oml':
		return render(request=request, template_name='recipe_basis/omlet.html', context={'com' : comr })
	elif comr == 'pas':
		return render(request=request, template_name='recipe_basis/pasta.html', context={'com' : comr })
	elif comr == 'but':
		return render(request=request, template_name='recipe_basis/buter.html', context={'com' : comr })
	elif comr == 'a':
		return render(request=request, template_name='recipe_basis/omlet.html', context={'com' : comr })
	else:
		print("repeat")
	return


