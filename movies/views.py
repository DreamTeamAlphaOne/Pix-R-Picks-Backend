from django.shortcuts import render
from .models import Movie
# from django.views.generic import ListView
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import MovieSerializer

# class MovieListView(ListView):
#     template_name ='movie_list.html'
#     model = Movie

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetails(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer