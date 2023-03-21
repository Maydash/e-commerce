from django.shortcuts import render
from shop.models import Category

def index(request):
    return render (request, 'index.html')

def contact(request):
    return render (request, 'contact.html')
