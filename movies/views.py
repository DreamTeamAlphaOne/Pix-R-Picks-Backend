from django.shortcuts import render
from .models import Movie
from rest_framework import generics
from .serializers import MovieSerializer
from .permissions import IsOwnerOrReadOnly
import random
from rest_framework import response
from rest_framework import status

# from rest_framework.permissions import IsAuthenticatedOrReadOnly

movie_scores = {'a bugs life':{'happy': 0.08, 'angry': 0.08, 'surprise': 0.32, 'sad': 0.22, 'fear': 0.29}, 'brave':{'happy': 0.11, 'angry': 0.1, 'surprise': 0.18, 'sad': 0.28, 'fear': 0.33}, 'cars':{'happy': 0.14, 'angry': 0.06, 'surprise': 0.31, 'sad': 0.25, 'fear': 0.25}, 'cars 2':{'happy': 0.1, 'angry': 0.08, 'surprise': 0.26, 'sad': 0.22, 'fear': 0.35}, 'cars 3':{'happy': 0.12, 'angry': 0.06, 'surprise': 0.24, 'sad': 0.26, 'fear': 0.31}, 'coco':{'happy': 0.08, 'angry': 0.08, 'surprise': 0.28, 'sad': 0.23, 'fear': 0.32}, 'finding dory':{'happy': 0.09, 'angry': 0.09, 'surprise': 0.27, 'sad': 0.24, 'fear': 0.32}, 'finding_nemo':{'happy': 0.11, 'angry': 0.09, 'surprise': 0.25, 'sad': 0.25, 'fear': 0.31}, 'the good dinosaur':{'happy': 0.12, 'angry': 0.08, 'surprise': 0.22, 'sad': 0.2, 'fear': 0.38}, 'the incredibles':{'happy': 0.1, 'angry': 0.09, 'surprise': 0.26, 'sad': 0.23, 'fear': 0.33}, 'the incredibles 2':{'happy': 0.13, 'angry': 0.07, 'surprise': 0.28, 'sad': 0.23, 'fear': 0.29}, 'inside out':{'happy': 0.13, 'angry': 0.06, 'surprise': 0.21, 'sad': 0.31, 'fear': 0.29}, 'monsters inc':{'happy': 0.12, 'angry': 0.08, 'surprise': 0.29, 'sad': 0.2, 'fear': 0.31}, 'monsters university':{'happy': 0.12, 'angry': 0.1, 'surprise': 0.28, 'sad': 0.2, 'fear': 0.3}, 'onward':{'happy': 0.09, 'angry': 0.09, 'surprise': 0.28, 'sad': 0.2, 'fear': 0.35}, 'ratatouille':{'happy': 0.1, 'angry': 0.08, 'surprise': 0.25, 'sad': 0.25, 'fear': 0.32}, 'soul':{'happy': 0.11, 'angry': 0.06, 'surprise': 0.33, 'sad': 0.2, 'fear': 0.3},'toy story':{'happy': 0.07, 'angry': 0.08, 'surprise': 0.36, 'sad': 0.17, 'fear': 0.32}, 'toy story 2':{'happy': 0.1, 'angry': 0.05, 'surprise': 0.4, 'sad': 0.22, 'fear': 0.23}, 'toy story 3':{'happy': 0.09, 'angry': 0.09, 'surprise': 0.28, 'sad': 0.18, 'fear': 0.36}, 'toy story 4':{'happy': 0.11, 'angry': 0.08, 'surprise': 0.31, 'sad': 0.21, 'fear': 0.3}, 'up':{'happy': 0.08, 'angry': 0.14, 'surprise': 0.2, 'sad': 0.22, 'fear': 0.35}, 'wall-e':{'happy': 0.07, 'angry': 0.14, 'surprise': 0.21, 'sad': 0.19, 'fear': 0.39}}

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
        passed_emotion = self.request.query_params.get('emotion')
        #passed_emotion = ('sad')
        #return Movie.objects.all()
        return find_queryset(passed_emotion)


class MovieDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    