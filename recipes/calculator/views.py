from django.shortcuts import render
from calculator.module.classes import Calc


def index(request):
	return render(request=request, template_name='calculator/index.html', context={})


def calc(request):
	path_file = 'D:\\django-sites\\NetologeDjango\\first_project\\dj-homeworks\\1.2-requests-templates\\recipes\\recipe_basis\\files\\data.json'

	if request.POST.get('pasta'):

		response_obj = Calc(path_file, 'pasta', int(request.POST.get('pasta')))
		response = response_obj.calc()

	elif request.POST.get('omlet'):
		response_obj = Calc(path_file, 'omlet', int(request.POST.get('omlet')) )
		response = response_obj.calc()

	elif request.POST.get('buter'):
		response_obj = Calc(path_file, 'buter', int(request.POST.get('buter')) )
		response = response_obj.calc()

	return render(request=request, template_name='calculator/index.html', context={'recipe':response})
