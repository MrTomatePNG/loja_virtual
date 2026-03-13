from django.contrib.auth.models import User
from django.test import TestCase

from produtos.models import Categoria, Produto, ProdutoVariacao

from .models import ItemPedido, Pedido


class PedidoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="comprador", password="password123"
        )
        self.categoria = Categoria.objects.create(nome="Doces", slug="doces")
        self.produto = Produto.objects.create(
            nome="Brigadeiro", slug="brigadeiro", categoria=self.categoria
        )
        self.variacao = ProdutoVariacao.objects.create(
            produto=self.produto,
            nome="Tradicional",
            sku="BRIG-TRAD",
            preco=4.50,
            estoque=50,
        )

    def test_pedido_creation(self):
        """Testa se o pedido e seus itens são criados corretamente."""
        pedido = Pedido.objects.create(usuario=self.user, endereco_entrega="Rua A, 123")
        item = ItemPedido.objects.create(
            pedido=pedido,
            produto_variacao=self.variacao,
            preco=self.variacao.preco,
            quantidade=10,
        )

        self.assertEqual(pedido.itens.count(), 1)
        self.assertEqual(pedido.get_total_cost(), 45.00)
        self.assertEqual(str(item), f"Item {item.id} do Pedido {pedido.id}")

    def test_pedido_status_default(self):
        """Testa se o status inicial do pedido é PENDENTE."""
        pedido = Pedido.objects.create(usuario=self.user, endereco_entrega="Rua A, 123")
        self.assertEqual(pedido.status, "PENDENTE")
