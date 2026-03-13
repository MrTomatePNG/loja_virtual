from django.shortcuts import get_object_or_404, render

from produtos.models import Produto


# Create your views here.
def listar_produtos(request):
    # Mostra apenas produtos que possuem pelo menos uma variação disponível
    produtos = Produto.objects.filter(variacoes__disponivel=True).distinct()
    return render(request, "produtos/lista.html", {"produtos": produtos})


def detalhes(request, slug):
    # Busca o produto pelo slug e garante que ele tenha variações disponíveis
    produto = get_object_or_404(Produto, slug=slug, variacoes__disponivel=True)
    return render(request, "produtos/detalhes.html", {"produto": produto})
