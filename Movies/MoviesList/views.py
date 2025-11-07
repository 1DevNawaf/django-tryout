from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def welcome_page(request):
    return render(request, 'base.html')