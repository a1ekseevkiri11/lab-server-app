from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('info/server/', views.infoServer),
    path('info/client/', views.infoClient),
    path('info/database', views.infoDatabase),
]
