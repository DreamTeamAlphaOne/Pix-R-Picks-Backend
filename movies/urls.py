from django.urls import path
from django.urls.resolvers import URLPattern
from .views import MovieListView

urlpatterns = [
    path('', MovieListView.as_view(), name="list_view"),
    
]