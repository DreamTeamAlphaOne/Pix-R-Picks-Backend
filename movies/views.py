from django.shortcuts import render
from .models import MovieSuggestion, MovieSelection
from rest_framework import generics
from .serializers import SelectionSerializer, SelectionSerializer, SuggestionSerializer
from .permissions import IsOwnerOrReadOnly

class MovieSuggestionList(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = MovieSuggestion.objects.all()
    serializer_class = SuggestionSerializer

class MovieSuggestionDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = MovieSuggestion.objects.all()
    serializer_class = SuggestionSerializer

class MovieSelectionList(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = MovieSelection.objects.all()
    serializer_class = SelectionSerializer

class MovieSelectionDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = MovieSelection.objects.all()
    serializer_class = SelectionSerializer
    