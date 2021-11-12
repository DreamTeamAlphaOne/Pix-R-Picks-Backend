from django.shortcuts import render


from django.shortcuts import render
from .models import FavMovie
from rest_framework import generics
from .serializers import FavMovieSerializer
from .permissions import IsOwnerOrReadOnly


class FavMovieList(generics.ListAPIView):
    queryset = FavMovie.objects.all()
    serializer_class = FavMovieSerializer

class FavMovieDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = FavMovie.objects.all()
    serializer_class = FavMovieSerializer

    