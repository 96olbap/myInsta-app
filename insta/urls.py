from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'^search/', views.search_results, name='search_results'),
    path('register/', views.register, name = 'register'),

]