from django.db import models


class MusicBand(models.Model):
    name = models.CharField(max_length=100)
    year_of_foundation = models.IntegerField()
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    group = models.ForeignKey('MusicBand', null=True, on_delete=models.SET_NULL, related_name='album')

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    album = models.ForeignKey('Album', null=True, on_delete=models.SET_NULL, related_name='track')

    def __str__(self):
        return self.title
