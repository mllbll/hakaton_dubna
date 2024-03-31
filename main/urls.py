# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_values, name='input_values'),
    path('add_user/', views.add_user_page, name='add_user_page'),
    path('add_user_data/', views.add_user_data, name='add_user_data'),
]
