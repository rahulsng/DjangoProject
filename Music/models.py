from django.db import models

class Album(models.Model):                         #What does each album have. means Album is a table name
    artist = models.CharField(max_length =250)    #Artist is a column, means value stored in album table
    album_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 1000)
   

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length = 250)
    song_title = models.CharField(max_length = 250)
