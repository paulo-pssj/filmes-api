from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField()
    link = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo
