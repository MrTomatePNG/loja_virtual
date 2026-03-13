from django.contrib.auth.models import User
from django.db import models


class Cliente(models.Model):
    user: User = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="cliente"
    )  # type: ignore

    cpf = models.CharField("CPF", max_length=11, unique=True, blank=True, null=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True)
    endereco = models.TextField("Endereço de entrega", blank=True)
    data_nascimento = models.DateField("Data de nascimento", blank=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    objects = models.Manager()

    def __str__(self) -> str:
        nome = self.user.get_full_name() or self.user.username
        return f"{nome} - {self.cpf if self.cpf else 'Sem CPF'}"
