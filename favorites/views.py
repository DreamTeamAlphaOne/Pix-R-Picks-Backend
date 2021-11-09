from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import FavMovie
from rest_framework import generics
from .serializers import FavMovieSerializer
from .permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

class FavMovieList(generics.ListAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = FavMovie.objects.all()
    serializer_class = FavMovieSerializer

class FavMovieDetails(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsOwnerOrReadOnly,)
    queryset = FavMovie.objects.all()
    serializer_class = FavMovieSerializer

    