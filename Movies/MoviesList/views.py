from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def Movie_Name(request):
    name = request.GET.get('name') or "Harry Potter"
    return render(request, "base.html", {"name":name})


def welcome_page(request):
    message = (f"<html> <h1> Welcome to the Movies List </h1> "
              f"<p> MoviesList has {Movie.objects.count()} Movies</p>"
              f"</html>")

    return HttpResponse(message)