from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from .models import ItemPedido, Pedido


class ItemPedidoInline(TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ["produto_variacao", "preco", "quantidade"]


@admin.register(Pedido)
class PedidoAdmin(ModelAdmin):
    list_display = [
        "id",
        "usuario",
        "criado_em",
        "status",
        "pago",
        "get_total_cost",
    ]
    list_filter = ["status", "pago", "criado_em"]
    list_editable = ["status", "pago"]
    inlines = [ItemPedidoInline]
    search_fields = ["usuario__username", "usuario__first_name", "id"]
