from django.test import TestCase

from produtos.models import Categoria, Produto


class ProdutoTestCase(TestCase):
    def setUp(self):
        # roda antes de cada teste — evita repetição
        self.categoria = Categoria.objects.create(nome="Geral", slug="geral")

    def test_create_produto(self):
        produto = Produto.objects.create(
            nome="Sabão", preco=5, categoria=self.categoria
        )
        self.assertIsInstance(produto, Produto)

    def test_update_produto(self):
        produto = Produto.objects.create(
            nome="Sabão", preco=5, categoria=self.categoria
        )
        produto.nome = "Detergente"
        produto.save()
        self.assertEqual(produto.nome, "Detergente")

    def test_update_preco(self):
        produto = Produto.objects.create(
            nome="Sabão", preco=5, categoria=self.categoria
        )
        produto.preco = 10
        produto.save()
        self.assertEqual(produto.preco, 10)

    def test_update_estoque(self):
        produto = Produto.objects.create(
            nome="Sabão", preco=5, categoria=self.categoria
        )
        produto.estoque = 10
        produto.save()
        self.assertEqual(produto.estoque, 10)

    def test_delete_produto(self):
        produto = Produto.objects.create(
            nome="Sabão", preco=5, categoria=self.categoria
        )
        produto.delete()
        self.assertEqual(Produto.objects.count(), 0)


class CategoriaTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Geral", slug="geral")

    def test_create_categoria(self):
        self.assertIsInstance(self.categoria, Categoria)

    def test_update_categoria(self):
        self.categoria.nome = "Limpeza"
        self.categoria.save()
        self.assertEqual(self.categoria.nome, "Limpeza")

    def test_delete_categoria(self):
        self.categoria.delete()
        self.assertEqual(Categoria.objects.count(), 0)

    def test_find_categoria(self):
        encontrada = Categoria.objects.get(slug="geral")
        self.assertIsInstance(encontrada, Categoria)

    def test_find_produtos_by_categoria(self):
        Produto.objects.create(nome="Sabão", preco=5, categoria=self.categoria)
        produtos = self.categoria.produtos.all()  # usa o related_name
        self.assertEqual(len(produtos), 1)
        self.assertIsInstance(produtos[0], Produto)

    def test_find_categoria_by_produto(self):
        produto = Produto.objects.create(
            nome="Sabão", preco=5, categoria=self.categoria
        )
        self.assertIsInstance(produto.categoria, Categoria)
