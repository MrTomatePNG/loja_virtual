from django.contrib.auth.models import User
from django.db import models

from produtos.models import ProdutoVariacao


class Pedido(models.Model):
    STATUS_CHOICES = (
        ("PENDENTE", "Pendente"),
        ("PREPARANDO", "Em Preparação"),
        ("ENVIADO", "Enviado"),
        ("ENTREGUE", "Entregue"),
        ("CANCELADO", "Cancelado"),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos")
    endereco_entrega = models.TextField("Endereço de Entrega")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    pago = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDENTE")

    objects = models.Manager()

    class Meta:
        ordering = ("-criado_em",)
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.get_full_name() or self.usuario.username}"  # type: ignore

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.itens.all())  # type: ignore


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name="itens", on_delete=models.CASCADE)
    produto_variacao = models.ForeignKey(
        ProdutoVariacao, related_name="itens_pedido", on_delete=models.CASCADE
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    objects = models.Manager()

    def __str__(self):
        return f"Item {self.id} do Pedido {self.pedido.id}"  # type: ignore

    def get_cost(self):
        return self.preco * self.quantidade  # type: ignore
