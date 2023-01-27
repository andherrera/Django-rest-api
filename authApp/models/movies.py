from django.db import models
from .user import User

STATUS = [
    ('public', 'public'),
    ('private', 'private'),
    ]

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length = 70, blank=False)    
    director = models.CharField('Director', max_length = 70, blank=False)
    genre = models.CharField('Genre', max_length = 40, blank=False)
    year = models.IntegerField('Year', blank=False)
    budget = models.IntegerField('Budget', blank=False)
    status = models.CharField(choices=STATUS, blank=False, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



