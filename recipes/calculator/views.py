from django.shortcuts import render
from django.http import HttpResponse
from urllib import request

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
	print(request.META.get('CSRF_COOKIE'))

	return render(request=request, template_name='calculator/index.html', context={})