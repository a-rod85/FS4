from django.contrib import admin
from django.urls import path
from main.views import get_main_page
from . import views


app_name = 'meals/'
urlpatterns = [
    path('', view.meal_list),
    path('', get_main_page, name='get_main_page')

]
