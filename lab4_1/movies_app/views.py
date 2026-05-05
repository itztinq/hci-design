from django.shortcuts import render, get_object_or_404

from movies_app.models import Movie

def index(request):
    all_movies = Movie.objects.all()
    context = {"movies": all_movies, "pageTitle": "Movie Application"}
    return render(request, 'index.html', context)

def details(request, id):
    movie = get_object_or_404(Movie, id=id)
    context = {"movie": movie}
    return render(request, 'movie_details.html', context)