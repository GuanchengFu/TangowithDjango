from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm
# Create your views here.


def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	context_dict['categories'] = category_list
	context_dict['pages'] = page_list
	return render(request, 'rango/index.html', context = context_dict)


def about(request):
	context_dict = {'name': 'This tutorial has been put together by Guancheng Fu'}
	return render(request, 'rango/about.html', context = context_dict)


def show_category(request, category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug = category_name_slug)

		pages = Page.objects.filter(category = category)

		context_dict['pages'] = pages

		context_dict['category'] = category
	except Category.DoesNotExist:

		context_dict['category'] = None
		context_dict['pages'] = None


	return render(request, 'rango/category.html', context_dict)


def add_category(request):
	form = CategoryForm()

	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit = True)

			return index(request)

		else:
			print(form.errors)


	return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
	try:
		category = Category.objects.get(slug = category_name_slug)
	except Category.DoesNotExist:
		category = None

	form = PageForm()
	if request.method == 'POST':