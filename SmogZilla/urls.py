from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add/', views.addReview, name = 'add review'),
    path('app/', views.app, name = 'app')
]