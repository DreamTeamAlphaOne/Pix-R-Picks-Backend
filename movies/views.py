from django.shortcuts import render
from .models import MovieSuggestion, MovieSelection
from rest_framework import generics
from .serializers import SelectionSerializer, SelectionSerializer, SuggestionSerializer

class MovieSuggestionList(generics.ListAPIView):
    queryset = MovieSuggestion.objects.all()
    serializer_class = SuggestionSerializer

class MovieSuggestionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieSuggestion.objects.all()
    serializer_class = SuggestionSerializer

class MovieSelectionList(generics.ListAPIView):
    queryset = MovieSelection.objects.all()
    serializer_class = SelectionSerializer

class MovieSelectionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieSelection.objects.all()
    serializer_class = SelectionSerializer
    