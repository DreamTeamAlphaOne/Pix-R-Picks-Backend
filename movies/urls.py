from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import MovieList, MovieDetails

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetails.as_view(), name='movie_details'),
    
]