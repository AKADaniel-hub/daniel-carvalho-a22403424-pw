from django.contrib import admin
from .models import Receita, Ingrediente

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tempo_preparo")


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "quantidade", "receita")