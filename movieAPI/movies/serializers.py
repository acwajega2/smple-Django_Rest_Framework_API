from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
     class Meta:
         model = Movie
         fields =('id','title','production_company')

class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Movie.objects.all())

    class Meta:
        model = Movie
        fields = ('id', 'username', 'movies')