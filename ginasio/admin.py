from django.contrib import admin
from .models import Cliente, Plano

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade")
    search_fields = ("nome",)


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco")