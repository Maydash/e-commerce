from django.urls import path
from .views import *



urlpatterns = [
    path('<str:slug>/', category, name='category'),
]