from django.db import models
from django.db.models import Index


class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        indexes = [
            Index(fields=["nome"]),
        ]

    objects = models.Manager()

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    descricao_geral = models.TextField("Descrição Geral", blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="produtos"
    )
    imagem_principal = models.ImageField(upload_to="produtos/%Y/%m/%d", blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "produto"
        verbose_name_plural = "produtos"
        indexes = [Index(fields=["nome"]), Index(fields=["categoria"])]

    objects = models.Manager()

    def __str__(self):
        return self.nome


class ProdutoVariacao(models.Model):
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name="variacoes"
    )
    nome = models.CharField("Sabor/Tamanho", max_length=200)
    sku = models.CharField("SKU/Código", max_length=50, unique=True)
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField("Estoque Atual", default=0)
    disponivel = models.BooleanField("Disponível para venda", default=True)
    imagem = models.ImageField(upload_to="produtos/variacoes/%Y/%m/%d", blank=True)

    class Meta:
        verbose_name = "Variação de Produto"
        verbose_name_plural = "Variações de Produtos"

    objects = models.Manager()

    def __str__(self):
        return f"{self.produto.nome} - {self.nome}"  # type: ignore
