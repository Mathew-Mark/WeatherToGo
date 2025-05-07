from django.contrib import admin
from django.urls import path

# importing views from views.py
from .views import local_weather

urlpatterns = [
    path('', local_weather),
]