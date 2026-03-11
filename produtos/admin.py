from django.contrib import admin

from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug"]
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
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
