from django.views.generic import ListView, DetailView
from .models import Movie

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/detail.html'
    context_object_name = 'movie'
