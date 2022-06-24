from django.urls import path
from . import views

urlpatterns = [
path('', views.call_login, name= 'login'),
path('main_page/', views.call_main, name = 'main_page')
]