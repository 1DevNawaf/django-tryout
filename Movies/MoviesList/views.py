from django.shortcuts import render
from .models import Movie

def welcome_page(request):
    return render(request, 'MoviesList/welcome.html')

def movies_list(request):
    movies = Movie.objects.all()
    context = {
        'movies_list': movies,
    }
    return render(request, 'MoviesList/movies_list.html', context)