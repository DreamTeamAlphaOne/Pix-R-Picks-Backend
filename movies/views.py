from django.shortcuts import render
from .models import Movie
from rest_framework import generics
from .serializers import MovieSerializer
from .permissions import IsOwnerOrReadOnly
import random
from rest_framework import response
from rest_framework import status

# from rest_framework.permissions import IsAuthenticatedOrReadOnly

movie_scores = {'a bugs life':{'Happy': 0.08, 'Angry': 0.08, 'Surprise': 0.32, 'Sad': 0.22, 'Fear': 0.29}, 'brave':{'Happy': 0.11, 'Angry': 0.1, 'Surprise': 0.18, 'Sad': 0.28, 'Fear': 0.33}, 'cars':{'Happy': 0.14, 'Angry': 0.06, 'Surprise': 0.31, 'Sad': 0.25, 'Fear': 0.25}, 'cars 2':{'Happy': 0.1, 'Angry': 0.08, 'Surprise': 0.26, 'Sad': 0.22, 'Fear': 0.35}, 'cars 3':{'Happy': 0.12, 'Angry': 0.06, 'Surprise': 0.24, 'Sad': 0.26, 'Fear': 0.31}, 'coco':{'Happy': 0.08, 'Angry': 0.08, 'Surprise': 0.28, 'Sad': 0.23, 'Fear': 0.32}, 'finding dory':{'Happy': 0.09, 'Angry': 0.09, 'Surprise': 0.27, 'Sad': 0.24, 'Fear': 0.32}, 'finding_nemo':{'Happy': 0.11, 'Angry': 0.09, 'Surprise': 0.25, 'Sad': 0.25, 'Fear': 0.31}, 'the good dinosaur':{'Happy': 0.12, 'Angry': 0.08, 'Surprise': 0.22, 'Sad': 0.2, 'Fear': 0.38}, 'the incredibles':{'Happy': 0.1, 'Angry': 0.09, 'Surprise': 0.26, 'Sad': 0.23, 'Fear': 0.33}, 'the incredibles 2':{'Happy': 0.13, 'Angry': 0.07, 'Surprise': 0.28, 'Sad': 0.23, 'Fear': 0.29}, 'inside out':{'Happy': 0.13, 'Angry': 0.06, 'Surprise': 0.21, 'Sad': 0.31, 'Fear': 0.29}, 'monsters inc':{'Happy': 0.12, 'Angry': 0.08, 'Surprise': 0.29, 'Sad': 0.2, 'Fear': 0.31}, 'monsters university':{'Happy': 0.12, 'Angry': 0.1, 'Surprise': 0.28, 'Sad': 0.2, 'Fear': 0.3}, 'onward':{'Happy': 0.09, 'Angry': 0.09, 'Surprise': 0.28, 'Sad': 0.2, 'Fear': 0.35}, 'ratatouille':{'Happy': 0.1, 'Angry': 0.08, 'Surprise': 0.25, 'Sad': 0.25, 'Fear': 0.32}, 'soul':{'Happy': 0.11, 'Angry': 0.06, 'Surprise': 0.33, 'Sad': 0.2, 'Fear': 0.3},'toy story':{'Happy': 0.07, 'Angry': 0.08, 'Surprise': 0.36, 'Sad': 0.17, 'Fear': 0.32}, 'toy story 2':{'Happy': 0.1, 'Angry': 0.05, 'Surprise': 0.4, 'Sad': 0.22, 'Fear': 0.23}, 'toy story 3':{'Happy': 0.09, 'Angry': 0.09, 'Surprise': 0.28, 'Sad': 0.18, 'Fear': 0.36}, 'toy story 4':{'Happy': 0.11, 'Angry': 0.08, 'Surprise': 0.31, 'Sad': 0.21, 'Fear': 0.3}, 'up':{'Happy': 0.08, 'Angry': 0.14, 'Surprise': 0.2, 'Sad': 0.22, 'Fear': 0.35}, 'wall-e':{'Happy': 0.07, 'Angry': 0.14, 'Surprise': 0.21, 'Sad': 0.19, 'Fear': 0.39}}

def find_movies_from_emotions(scores_dict, emotion, number_of_recs):
    '''function to return a specified number of movies associated with a given emotion'''
    top_6_dict = {}
    def find_dict_minimum(dictionary):
        '''function to find the minimum value in a dictionary'''
        minimum = 1.0
        for item in dictionary:
            if dictionary[item] < minimum:
                minimum = dictionary[item]
        return minimum
    
    def get_key_with_min(dictionary):
        '''function to find the key associated with the minimum value in a dictionary'''
        for item in dictionary:
            if dictionary[item] == find_dict_minimum(dictionary):
                return item
    def get_random_results(dictionary):
        '''function that returns a specified number of random movie names from a dictionary'''
        movies = dictionary.keys()
        rand_movies = random.sample(movies, k = number_of_recs)
        return rand_movies
    
    for movie in scores_dict:
        #pushes the first 6 movies into holding dictionary with name as key and score of given emotion as value
        if len(top_6_dict) <= 8:
            top_6_dict[movie] = scores_dict[movie][emotion]
        if len(top_6_dict) > 8:
            #checks to see if movie's score for given emotion is higher than the lowest value of chosen emotion in holding dictionary
            if find_dict_minimum(top_6_dict) < scores_dict[movie][emotion]:
                #replaces movie with lowest score
                top_6_dict[movie] = scores_dict[movie][emotion]
                top_6_dict.pop(get_key_with_min(top_6_dict))
            
    
    #print(top_6_dict)
    return list(get_random_results(top_6_dict))



def find_queryset(emotion):
    get_movie_list = find_movies_from_emotions(movie_scores, emotion, 1)
    
    def get_movie(movie_list):
        for movie in movie_list:
            return movie
    
    get_single_movie = get_movie(get_movie_list)
    queryset = Movie.objects.all().filter(title=get_single_movie.lower())
    return queryset



class MovieList(generics.ListAPIView):

    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = MovieSerializer


    def get_queryset(self):
        #passed_emotion = self.request.query_params.get('emotion')
        passed_emotion = ('Sad')
        #return Movie.objects.all()
        return find_queryset(passed_emotion)


class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    