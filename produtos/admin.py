from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from .models import Categoria, Produto, ProdutoVariacao


class ProdutoVariacaoInline(StackedInline):
    model = ProdutoVariacao
    extra = 1  # Mostra uma linha em branco para nova variação
    verbose_name = "Variação de Doce"
    verbose_name_plural = "Variações (Sabores/Tamanhos)"


@admin.register(Categoria)
class CategoriaAdmin(ModelAdmin):
    list_display = ["nome", "slug"]
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Produto)
class ProdutoAdmin(ModelAdmin):
    list_display = ["nome", "categoria"]
    prepopulated_fields = {"slug": ("nome",)}
    inlines = [ProdutoVariacaoInline]


@admin.register(ProdutoVariacao)
class ProdutoVariacaoAdmin(ModelAdmin):
    list_display = ["produto", "nome", "sku", "preco", "estoque", "disponivel"]
    list_editable = ["preco", "estoque", "disponivel"]
    search_fields = ["nome", "sku", "produto__nome"]
