from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    img_path = models.CharField(max_length=500)
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    mpaa_type = models.CharField(max_length=10)
    mpaa_label = models.CharField(max_length=100)
    user_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.name
