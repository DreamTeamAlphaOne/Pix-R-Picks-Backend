from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class MovieSuggestion(models.Model):
    """Model representing the individual Movie Objects we will be suggesting to the users"""
    title = models.CharField(max_length=64)
    description = models.TextField(default='')
    emotion_score = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])
    
class MovieSelection(models.Model):
    """ Model representing the selected Movie Objects the users want to save to their own lists """
    movie = models.ForeignKey('MovieSuggestion', on_delete=models.RESTRICT, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'Saved Selection: {self.movie.title}'

