from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Movie
# Create your tests here.

class MovieTests(TestCase):

  @classmethod
  def setUpTestData(cls):
    testuser1 = get_user_model().objects.create_user(username='tester1', password='pass')
    testuser1.save()

    test_movie = Movie.objects.create(
      title='Pixar Movie',
      description='incredibly touching and kinda sad',
      emotion_score='{"happy": 0.08, "angry": 0.08, "surprise": 0.28, "sad": 0.23, "fear": 0.32}'
    )
    test_movie.save()

  def test_movie_content(self):
    movie = Movie.objects.get(id=1)
    actual_title = str(movie.title)
    actual_description = str(movie.description)
    actual_emotion_score = str(movie.emotion_score)
    self.assertEqual(actual_title,'Pixar Movie')
    self.assertEqual(actual_description,'incredibly touching and kinda sad')

    
