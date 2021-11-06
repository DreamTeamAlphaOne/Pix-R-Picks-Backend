from rest_framework import serializers
from .models import MovieSuggestion, MovieSelection

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'description', 'emotion_score')
        model = MovieSuggestion

class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('movie', 'user')
        model = MovieSelection
        