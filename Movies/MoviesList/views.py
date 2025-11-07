from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def welcome_page(request):
    return render(request, 'base.html')

def movies_list(request):
    movies = Movie.objects.all()
    context = {
        'movies_list': movies,
    }
    return render(request, 'MoviesList/movies_list.html', context)