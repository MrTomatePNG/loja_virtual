from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from produtos.models import ProdutoVariacao

from .cart import Carrinho


@require_POST
def adicionar_ao_carrinho(request, variacao_id):
    """View para adicionar uma variação de doce ao carrinho via POST."""
    carrinho = Carrinho(request)
    variacao = get_object_or_404(ProdutoVariacao, id=variacao_id)
    carrinho.adicionar(variacao=variacao)
    return redirect("carrinho:detalhe_carrinho")


@require_POST
def remover_do_carrinho(request, variacao_id):
    """View para remover uma variação de doce do carrinho via POST."""
    carrinho = Carrinho(request)
    variacao = get_object_or_404(ProdutoVariacao, id=variacao_id)
    carrinho.remover(variacao)
    return redirect("carrinho:detalhe_carrinho")


def detalhe_carrinho(request):
    """View para listar todos os doces no carrinho."""
    carrinho = Carrinho(request)
    return render(request, "carrinho/detalhe.html", {"carrinho": carrinho})
