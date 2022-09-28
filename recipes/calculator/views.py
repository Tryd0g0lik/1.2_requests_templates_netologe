from django.shortcuts import render
from django.http import HttpResponse
from urllib import request

from calculator.module.classes import Calc

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }



def index(request):
	print("222222222")
	# print(request.META.get('CSRF_COOKIE'))

	return render(request=request, template_name='calculator/index.html', context={})

def calc(request):
	path_file = 'D:\\django-sites\\NetologeDjango\\first_project\\dj-homeworks\\1.2-requests-templates\\recipes\\recipe_basis\\files\\data.json'


	if request.POST.get('pasta'):
		# print(f"44444444 {requet.POST.get('pasta')}")
		response_obj = Calc(path_file, 'pasta', int(request.POST.get('pasta')) )
		response = response_obj.calc()
		# print(f"55888 {response}")
	elif request.POST.get('omlet'):
		response_obj = Calc(path_file, 'omlet', int(request.POST.get('omlet')) )
		response = response_obj.calc()
	elif request.POST.get('buter'):
		response_obj = Calc(path_file, 'buter', int(request.POST.get('buter')) )
		response = response_obj.calc()


	return render(request=request, template_name='calculator/index.html', context={'recipe':response})

