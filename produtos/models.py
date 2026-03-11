from django.db import models


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

    objects: type[models.Manager["Categoria"]]


# Nota: um produto pode ter várias categorias
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="produtos"
    )

    class Meta:
        ordering = ["nome"]
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    objects: type[models.Manager["Produto"]]

    def __str__(self):
        return self.nome
