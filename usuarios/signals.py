from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from usuarios.models import Cliente


@receiver(post_save, sender=User)
def create_cliente(sender, instance, created, **kwargs):
    if created:
        # Usamos get_or_create para evitar o IntegrityError com o Admin Inlines
        Cliente.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def salvar_perfil_cliente(sender, instance, **kwargs):
    if hasattr(instance, "cliente"):
        instance.cliente.save()
