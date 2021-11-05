from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import MovieSuggestionList, MovieSuggestionDetails, MovieSelectionList, MovieSelectionDetails

urlpatterns = [
    path('', MovieSuggestionList.as_view(), name='suggestion_list'),
    path('<int:pk>/', MovieSuggestionDetails.as_view(), name='suggestion_details'),
    path('saved/', MovieSelectionList.as_view(), name='selection_list'),
    path('saved/<int:pk>/', MovieSelectionDetails.as_view(), name='selection_details'),
]