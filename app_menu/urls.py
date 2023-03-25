from django.urls import path

from .models import MenuItem
from .views import index, menu_item_detail

app_name = 'draw'

urlpatterns = [
    path('', index, {'names': MenuItem.objects.filter(parent__isnull=True)}, name='index'),
    path('<str:menu_item_name>/', menu_item_detail, name='menu_item_detail'),
                ]
