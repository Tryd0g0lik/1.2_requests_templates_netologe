import html
from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from recipe_basis.module.menu import Menu
from recipe_basis.module.basis_recipe import Basis, recipes
import json
from urllib import request
from django.template import loader
# Create your views here.

def menuMain(request):

	fileName = "recipes/recipe_basis/files/data.json"
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
	rend = render(request=request, template_name='recipe_basis/index.html', context={'text' : main_menu})
	if request.POST.get("main"):
		return rend
	return rend








def omlet(request):
	# current_name = forms.CharField(label='Your name', max_length=100)
	comr = request.POST.get('command')
	fileName = "D:\\django-sites\\NetologeDjango\\first_project\\dj-homeworks\\1.2-requests-templates\\recipes\\recipe_basis\\files\\data.json"
	if comr == 'oml':
		with open(file=fileName, encoding="utf-8", mode='r') as file:

			lists = dict(json.load(file))['omlet']
			print(lists)
			k = list(dict(lists).keys())
			v = list(dict(lists).values())
			lists = list(zip(k, v))
		# lists = [list(dict(r).values())[2] for r in Basis(f) if comr == list(dict(r).keys())[0][:3]]
		return render(request=request, template_name='recipe_basis/omlet.html', context={'com' : 'omlet',
		                                                                                 'lists' : lists})
		# ------- -------- -------
	elif comr == 'pas':
		with open(file=fileName, encoding="utf-8", mode='r') as file:
			lists = dict(json.load(file))['pasta']
			print(lists)
			k = list(dict(lists).keys())
			v = list(dict(lists).values())
			lists = list(zip(k, v))
		return render(request=request, template_name='recipe_basis/pasta.html', context={'com' : 'pasta',
		                                                                                 'lists' : lists})

	# ------- -------- -------
	elif comr == 'but':
		with open(file=fileName, encoding="utf-8", mode='r') as file:
			lists = dict(json.load(file))['buter']
			print(lists)
			k = list(dict(lists).keys())
			v = list(dict(lists).values())
			lists = list(zip(k, v))
		return render(request=request, template_name='recipe_basis/buter.html', context={'com' : 'buter',
		                                                                                 'lists' : lists})

	# ------- -------- -------
	elif comr == 'a':
		obj_menu = Menu()
		menu = obj_menu.menu(fileName)

		main_menu = f"""
		Меню команды для выбора рецепта:; {menu[0]}
		""".split(";")

		with open(file=fileName, encoding="utf-8", mode='r') as file:
			lists = (json.load(file))
		return render(request=request, template_name='recipe_basis/index.html', context={'text' : main_menu,
		                                                                                 'com' : "Все что есть",
		                                                                                 'lists' : lists})
	else:
		print("repeat")
		return render(request=request, template_name='recipe_basis/index.html', context={})


