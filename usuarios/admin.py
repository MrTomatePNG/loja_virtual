from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from unfold.admin import ModelAdmin, StackedInline

from usuarios.models import Cliente

# Remove o registro original do User para substituir pelo Unfold
admin.site.unregister(User)


class ClienteInline(StackedInline):
    model = Cliente
    can_delete = False
    verbose_name_plural = "Dados Adicionais do Cliente"


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    inlines = (ClienteInline,)
    list_display = ("username", "email", "first_name", "last_name", "is_staff")


@admin.register(Cliente)
class ClienteAdmin(ModelAdmin):
    list_display = ("user", "cpf", "telefone")
    search_fields = ("user__username", "user__email", "cpf")
