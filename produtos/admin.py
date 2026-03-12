from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(ModelAdmin):
    list_display = ["nome", "slug"]
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Produto)
class ProdutoAdmin(ModelAdmin):
    list_display = [
        "nome",
        "slug",
        "preco",
        "estoque",
        "disponivel",
        "criado_em",
        "atualizado_em",
    ]
    list_filter = ["disponivel", "criado_em", "atualizado_em", "categoria"]
    list_editable = ["preco", "estoque", "disponivel"]
    prepopulated_fields = {"slug": ("nome",)}
