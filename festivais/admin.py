from django.contrib import admin
from .models import Festival, Artista

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome", "local")
    filter_horizontal = ("artistas",)


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero")