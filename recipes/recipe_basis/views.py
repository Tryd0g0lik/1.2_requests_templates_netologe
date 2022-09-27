import html
from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from recipe_basis.module.menu import Menu
from recipe_basis.module.basis_recipe import Basis


# Create your views here.
def menuMain(request):

	fileName = "data.json"
	"""
	Returns command's  a symbol for run a menu
	:param fileName: The file name there has recipes list
	:return:
	"""
	obj_menu = Menu()
	menu = obj_menu.menu(fileName)
	main_menu = f"""
Меню команды для выбора рецепта:; {menu[0]}
""".split(";")

	# inp = input(": ")
	# inp = (inp).strip().lower()
	# if len(inp) <= 3 and len(inp) > 0:
	# 		for i in range(0, len(menu[1]) -1):
	# 			if inp == menu[1][i]:
	# 				i






	return render(request=request, template_name='recipe_basis/index.html', context={'text' : main_menu})

# menuMain("data.json")

# Создать меню и запусть с переходом на страницу

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

