from django.shortcuts import render
from django.http import HttpResponse

from recipe_basis.module.menu import Menu
from recipe_basis.module.basis_recipe import Basis
import json
from urllib import request
from django.template import loader
# Create your views here.
# def menuMain(request) -> tuple:
def menuMain(request):
	fileName = "data.json"
	"""
	Returns a first element is a file name, the second element command's  the symbol for run a menu
	:param fileName: The file name there has recipes list
	:return:
	"""
	obj_menu = Menu()
	menu = obj_menu.menu(fileName)
	# 	print(f"""
	# Меню команды
	# {menu[0]}
	menu_response = f"""
Меню команды
{menu[0]}
Введите команду"""
	# templates = loader.get_template("recipe_basis\\templates\\index.html")
	# template = loader.get_template('recipe_basis/index.html')
	template = 'recipe_basis/index.html'
	# return render(request=request,  template_name="index.html")
	return render(request=request,  template_name=template, context={'menu' : menu_response})
	# inp = input(": ")
	#
	# inp = (inp).strip().strip("'").lower()
	# if len(inp) <= 3 and len(inp) > 0:
	# 	for i in range(0, len(menu[1])):
	# 		if inp == menu[1][i] and i < len(menu[1]):
	# 			return fileName, inp
	# 		# elif i >= len(menu[i]):
	# 		# 	print("Return and repeat")
	# 		# 	exit()
	# 		else:
	# 			continue


def recipe(request):

	return render(request=request, template_name='recipe_basis/recipe.html', context={})

# def recipe(request):
# 	comand = 'oml'
# 	fileName = "data.json"
	# try:
	# 	(fileName, comand) = menuMain(fileName)
	# except (Exception, BaseException, SyntaxError, NameError, TypeError):
	# 	print("Return and repeat")
	# 	exit()
	# with open(f"files\\{fileName}", mode="r", encoding="utf-8") as jsonFile:
	# 	for dict_var in Basis(json.load(jsonFile)):
	# 		if (dict_var)[0][0 : 3] == comand:
	# 			return dict_var

	# name = dict_var[0]
	# name_product = list(dict(dict_var[1]).keys())
	# product_count = list(dict(dict_var[1]).values())
	# product = list(zip(name_product, product_count)) # 'product' - it's the product list and a product count
	#
	# for string in product:
	# 	prod = list(dict(string).keys())[0]
	# 	prod_count = list(dict(string).values())[0]


	# return render( request, 'recipe_basis/recipe.html', context={"name": name,
 # "prod" : prod,
 # "prod_count" : prod_count})
	# return render(request=request,
	#               template_name='recipe_basis/recipe.html',
	#               context={"name" : fileName})

#

# name, prod, prod_count = recipe("DATA.json")


# Создать меню и запусть с переходом на страницу