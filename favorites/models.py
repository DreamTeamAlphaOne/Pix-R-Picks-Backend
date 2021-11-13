from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from movies.models import Movie


class FavMovie(models.Model):
    """ Model representing the selected Movie Objects the users want to save to their own lists """
    
    movie = models.ForeignKey(Movie, on_delete=models.RESTRICT, null=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie.title} -- {self.owner.email}'
    
    def get_absolute_url(self):
        return reverse('fav_movie_details', args=[str(self.id)])