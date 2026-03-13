from django.test import Client, TestCase
from django.urls import reverse

from produtos.models import Categoria, Produto, ProdutoVariacao


class CarrinhoTest(TestCase):
    def setUp(self):
        # Configuração inicial: Categoria -> Produto -> Variação (SKU)
        self.categoria = Categoria.objects.create(nome="Doces", slug="doces")
        self.produto = Produto.objects.create(
            nome="Brigadeiro", slug="brigadeiro", categoria=self.categoria
        )
        self.variacao = ProdutoVariacao.objects.create(
            produto=self.produto,
            nome="Pistache",
            sku="BRIG-PIS",
            preco=5.00,
            estoque=10,
        )
        self.client = Client()

    def test_adicionar_ao_carrinho_view(self):
        """Testa se a view de adicionar insere o doce na sessão."""
        url = reverse("carrinho:adicionar_ao_carrinho", args=[self.variacao.id])
        response = self.client.post(url)
        
        # Deve redirecionar para a página de detalhes do carrinho
        self.assertRedirects(response, reverse("carrinho:detalhe_carrinho"))
        
        # Verifica se o item está na sessão (o ID da variação é a chave)
        session = self.client.session
        from django.conf import settings
        self.assertIn(str(self.variacao.id), session[settings.CART_SESSION_ID])

    def test_remover_do_carrinho_view(self):
        """Testa se a view de remover retira o doce da sessão."""
        # Primeiro adiciona
        self.client.post(reverse("carrinho:adicionar_ao_carrinho", args=[self.variacao.id]))
        
        # Depois remove
        url = reverse("carrinho:remover_do_carrinho", args=[self.variacao.id])
        response = self.client.post(url)
        
        self.assertRedirects(response, reverse("carrinho:detalhe_carrinho"))
        
        # Verifica se a sessão está vazia para aquele ID
        session = self.client.session
        from django.conf import settings
        self.assertNotIn(str(self.variacao.id), session[settings.CART_SESSION_ID])

    def test_detalhe_carrinho_vazio(self):
        """Testa se a página do carrinho carrega corretamente quando vazio."""
        response = self.client.get(reverse("carrinho:detalhe_carrinho"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Seu carrinho está vazio")

    def test_detalhe_carrinho_com_itens(self):
        """Testa se a página do carrinho mostra os doces adicionados."""
        self.client.post(reverse("carrinho:adicionar_ao_carrinho", args=[self.variacao.id]))
        response = self.client.get(reverse("carrinho:detalhe_carrinho"))
        
        self.assertEqual(response.status_code, 200)
        # Verifica se o nome do doce e o subtotal aparecem no HTML
        self.assertContains(response, "Brigadeiro")
        self.assertContains(response, "Pistache")
        self.assertContains(response, "R$ 5.00")
