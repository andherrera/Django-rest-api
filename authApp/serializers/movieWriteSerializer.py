from rest_framework import serializers
from authApp.models.movies import Movie
from authApp.models.user import User

class MovieWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'