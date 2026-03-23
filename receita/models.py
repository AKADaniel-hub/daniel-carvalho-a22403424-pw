from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    tempo_preparo = models.IntegerField()

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=50)
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.receita.nome})"