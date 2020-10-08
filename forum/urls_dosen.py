from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.index_dosen),
    # path('new/', views.new),
    path('<id>/', views.detail_forum),
    path('<id>/delete/', views.delete_dosen),
    # path('<id>/update/', views.update),
    
]