from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()

    def __str__(self):
        return f"{self.nome} - {self.preco}€"