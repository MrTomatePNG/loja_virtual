from django.shortcuts import render

from produtos.models import Produto


# Create your views here.
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/lista.html", {"produtos": produtos})
