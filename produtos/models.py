from django.db import models
from django.db.models import Index


# Create your models here.
# Nota: uma categoria pode ter vários produtos
class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        indexes = [
            Index(fields=["nome"]),
        ]

    objects: type[models.Manager["Categoria"]]


# Nota: um produto pode ter várias categorias
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    disponivel = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, max_length=200)
    imagem = models.ImageField(upload_to="produtos/%Y/%m/%d", blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="produtos"
    )

    class Meta:
        ordering = ["nome"]
        verbose_name = "produto"
        verbose_name_plural = "produtos"
        indexes = [Index(fields=["nome"]), Index(fields=["categoria", "disponivel"])]

    objects: type[models.Manager["Produto"]]

    def __str__(self):
        return self.nome
