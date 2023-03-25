from django.shortcuts import render

# Create your views here.


def index(request, names):
    return render(request, 'index.html', {'names': names})


def menu_item_detail(request, menu_item_name):
    return render(request, 'index_detail.html', {'name': menu_item_name})