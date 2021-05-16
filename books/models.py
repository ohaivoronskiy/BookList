from django.conf import settings
from django.db import models

class Book(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    description = models.CharField(max_length=256)
    poster = models.ImageField(upload_to='posters', blank=True)

    def __str__(self):
        return self.title
