from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()

    rating = (
        (1, "worst"),
        (2, "bad"),
        (3, "not good"),
        (4, "good"),
        (5, "excellent"),
    )

    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name + " ,artist:" + str(self.artist)
