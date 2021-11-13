from rest_framework import serializers
from .models import FavMovie

class FavMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavMovie
        fields = "__all__"