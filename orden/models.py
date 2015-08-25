from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    entrada = models.TextField()
    salida = models.TextField()

    def __str__(self):
            return self.title