from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('delete/<int:roll>',views.delete_record,name="delete_record")
]
