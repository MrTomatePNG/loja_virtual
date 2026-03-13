from django.test import TestCase, override_settings
from django.urls import reverse

from .models import Categoria, Produto, ProdutoVariacao


class ProdutoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Doces Gourmet", slug="doces-gourmet")
        self.produto = Produto.objects.create(
            nome="Brigadeiro Gourmet",
            slug="brigadeiro-gourmet",
            descricao_geral="O melhor brigadeiro do universo.",
            categoria=self.categoria,
        )

    def test_produto_creation(self):
        """Testa se o produto pai foi criado corretamente."""
        self.assertEqual(str(self.produto), "Brigadeiro Gourmet")
        self.assertEqual(self.produto.slug, "brigadeiro-gourmet")

    def test_variacao_creation(self):
        """Testa se as variações (SKUs) estão vinculadas corretamente ao produto."""
        variacao = ProdutoVariacao.objects.create(
            produto=self.produto,
            nome="Sabor Pistache",
            sku="BRIG-PIS-01",
            preco=5.50,
            estoque=100,
        )
        self.assertEqual(str(variacao), "Brigadeiro Gourmet - Sabor Pistache")
        self.assertEqual(self.produto.variacoes.count(), 1)


@override_settings(ROOT_URLCONF="config.urls")
class ProdutoViewsTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Doces", slug="doces")
        self.produto = Produto.objects.create(
            nome="Coxinha de Morango",
            slug="coxinha-morango",
            categoria=self.categoria,
        )
        # Cria uma variação disponível
        ProdutoVariacao.objects.create(
            produto=self.produto,
            nome="Padrão",
            sku="COX-MOR-01",
            preco=12.00,
            estoque=10,
            disponivel=True,
        )

    def test_lista_produtos_view(self):
        """Testa se a vitrine carrega e lista os produtos."""
        url = reverse("produtos:lista-produtos")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Coxinha de Morango")

    def test_detalhes_produto_view(self):
        """Testa se a página de detalhes de um produto carrega via slug."""
        url = reverse("produtos:detalhes-produto", kwargs={"slug": "coxinha-morango"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Coxinha de Morango")

    def test_detalhes_produto_404(self):
        """Testa se acessar um slug inexistente retorna 404 limpo."""
        url = reverse("produtos:detalhes-produto", kwargs={"slug": "produto-que-nao-existe"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
