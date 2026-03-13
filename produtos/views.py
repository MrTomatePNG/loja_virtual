from django.shortcuts import get_object_or_404, render

from produtos.models import Produto


# Create your views here.
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/lista.html", {"produtos": produtos})


def detalhes(request, slug):
    produto = get_object_or_404(Produto, slug=slug)
    return render(request, "produtos/detalhes.html", {"produto": produto})
