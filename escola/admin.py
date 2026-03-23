from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "idade")
    search_fields = ("nome",)

admin.site.register(Aluno, AlunoAdmin)
