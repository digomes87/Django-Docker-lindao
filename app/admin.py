from app.models import Categoria
from django.contrib import admin


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["produto", "descricao"]
    search_fields = ["produto"]

admin.site.register(Categoria, CategoriaAdmin)