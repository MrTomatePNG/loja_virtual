from decimal import Decimal
from django.conf import settings
from produtos.models import ProdutoVariacao


class Carrinho:
    def __init__(self, request):
        """Inicializa o carrinho a partir da sessão do Django."""
        self.session = request.session
        carrinho = self.session.get(settings.CART_SESSION_ID)
        if not carrinho:
            # Cria um carrinho vazio na sessão se não existir
            carrinho = self.session[settings.CART_SESSION_ID] = {}
        self.carrinho = carrinho

    def adicionar(self, variacao, quantidade=1, override_quantidade=False):
        """Adiciona um item (SKU) ao carrinho ou atualiza sua quantidade."""
        variacao_id = str(variacao.id)
        if variacao_id not in self.carrinho:
            self.carrinho[variacao_id] = {
                "quantidade": 0,
                "preco": str(variacao.preco),
            }

        if override_quantidade:
            self.carrinho[variacao_id]["quantidade"] = quantidade
        else:
            self.carrinho[variacao_id]["quantidade"] += quantidade
        self.save()

    def save(self):
        """Marca a sessão como modificada para garantir que os dados sejam salvos."""
        self.session.modified = True

    def remover(self, variacao):
        """Remove uma variante de doce do carrinho."""
        variacao_id = str(variacao.id)
        if variacao_id in self.carrinho:
            del self.carrinho[variacao_id]
            self.save()

    def __iter__(self):
        """Itera sobre os itens do carrinho e busca os objetos do banco de dados."""
        variacao_ids = self.carrinho.keys()
        # Busca todas as variantes de uma vez para performance (RAD!)
        variacoes = ProdutoVariacao.objects.filter(id__in=variacao_ids)
        carrinho = self.carrinho.copy()

        for variacao in variacoes:
            carrinho[str(variacao.id)]["produto_variacao"] = variacao

        for item in carrinho.values():
            item["preco"] = Decimal(item["preco"])
            item["total_preco"] = item["preco"] * item["quantidade"]
            yield item

    def __len__(self):
        """Conta o total de unidades de doces no carrinho."""
        return sum(item["quantidade"] for item in self.carrinho.values())

    def get_total_preco(self):
        """Calcula o valor total de todos os itens no carrinho."""
        return sum(
            Decimal(item["preco"]) * item["quantidade"] for item in self.carrinho.values()
        )

    def limpar(self):
        """Esvazia o carrinho de doces."""
        del self.session[settings.CART_SESSION_ID]
        self.save()
