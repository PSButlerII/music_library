from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50, blank=True)
    artist = models.CharField(max_length=50, blank=True)
    album = models.CharField(max_length=50, blank=True)
    release_date = models.DateTimeField(blank=True)
    song_likes = models.ManyToManyField(User, default=None, blank=True)
    song_like_counter = models.PositiveBigIntegerField(default=0, blank=True)


# CRUD
# Create / insert / add - POST
# Retrieve / fetch - GET
# Update / edit - PUT
# Delete / remove - DELETE
