from django.db import models


# Create your models here.
class Song(models.Model):

    """Docstring for Song. Ovaj model ce sadrzati dva modela ime pesme,
       i FileField za hendlovanje pesmama.
       This app will contain two model fields, one name of the tracks,
       and FileField to handle are songs."""
    song_name = models.CharField(max_length=128)
    audio_file = models.FileField()
