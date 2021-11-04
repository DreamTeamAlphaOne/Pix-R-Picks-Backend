from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'description', 'score', 'dateAdded', 'owner')
        model = Movie
        