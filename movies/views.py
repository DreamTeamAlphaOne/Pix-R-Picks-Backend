from django.shortcuts import render
from .models import Movie
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import ListView

class MovieListView(ListView):
    template_name ='movie_list.html'
    model = Movie


