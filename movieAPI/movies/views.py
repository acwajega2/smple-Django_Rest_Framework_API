from django.shortcuts import render


from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer,UserSerializer 
from django.http import HttpResponse
from django.contrib.auth.models import User # new


# Create your views here.
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UserList(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer






def index (request):
    return HttpResponse('Hello from movie ass  APP--INDEX VIEW!')