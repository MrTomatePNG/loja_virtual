from django.shortcuts import get_object_or_404, render

from produtos.models import Produto


# Create your views here.
def listar_produtos(request):
    # Mostra apenas produtos disponíveis na vitrine
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, "produtos/lista.html", {"produtos": produtos})


def detalhes(request, slug):
    # Usa get_object_or_404 para evitar o erro DoesNotExist
    produto = get_object_or_404(Produto, slug=slug, disponivel=True)
    return render(request, "produtos/detalhes.html", {"produto": produto})

