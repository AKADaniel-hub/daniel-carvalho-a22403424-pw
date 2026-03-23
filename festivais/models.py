from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Festival(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    artistas = models.ManyToManyField(Artista)

    def __str__(self):
        return self.nome