from django.shortcuts import render

def Movie_Name(request):
    name = request.GET.get('name') or "Harry Potter"
    return render(request, "base.html", {"name":name})


