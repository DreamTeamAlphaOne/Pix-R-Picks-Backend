from django.db import models
from django.urls import reverse

class Movie(models.Model):
    """Model representing the individual Movie Objects we will be suggesting to the users"""
    title = models.CharField(primary_key=True, max_length=64)
    description = models.TextField(default="")
    image_url = models.URLField(max_length=1000)
    emotion_score = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_details', args=[str(self.id)])


