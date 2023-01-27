from rest_framework import serializers
from authApp.models.movies import Movie
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class MovieReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Movie
        fields = '__all__'
        #depth = 1