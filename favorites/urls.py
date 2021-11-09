from django.urls import path
from .views import FavMovieList, FavMovieDetails

urlpatterns = [
    path('', FavMovieList.as_view(), name='fav_movie_list'),
    path('<int:pk>/', FavMovieDetails.as_view(), name='fav_movie_details'),
    
]