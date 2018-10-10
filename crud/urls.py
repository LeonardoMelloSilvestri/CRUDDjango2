from django.contrib import admin
from django.urls import path, include
from .views import home, new, update, delete

urlpatterns = [
    path('', home, name="show"),
    path('new', new, name="create"),
    path('update/<int:pk>', update, name="edit"),
    path('delete/<int:pk>', delete, name="exclude")
]
