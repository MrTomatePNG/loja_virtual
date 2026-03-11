from django.shortcuts import render

from produtos.models import Produto


# Create your views here.
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/lista.html", {"produtos": produtos})


def detalhes(request, slug):
    produto: Produto = Produto.objects.get(slug=slug)
    return render(request, "produtos/detalhes.html", {"produto": produto})
