from django.shortcuts import render
from .models import Movie
from rest_framework import generics
from .serializers import MovieSerializer
from .permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MovieList(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    