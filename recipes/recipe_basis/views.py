from django.shortcuts import render
from django.http import HttpResponse
from recipes.recipe_basis.module.menu import Menu
from recipes.recipe_basis.module.basis_recipe import Basis


# Create your views here.
def menuMain(fileName : str):
	"""
	Returns command's  a symbol for run a menu
	:param fileName: The file name there has recipes list
	:return:
	"""
	obj_menu = Menu()
	menu = obj_menu.menu(fileName)
	print(f"""
Меню команды
{menu[0]}

Введите команду""")

	# inp = input(": ")
	# inp = (inp).strip().lower()
	# if len(inp) <= 3 and len(inp) > 0:
	# 		for i in range(0, len(menu[1]) -1):
	# 			if inp == menu[1][i]:
	# 				i






	return menu

menuMain("DATA.json")

# Создать меню и запусть с переходом на страницу