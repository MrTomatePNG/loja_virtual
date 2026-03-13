from django.shortcuts import render


# Create your views here.
def carrinho_view(request):
    return render(request, "carrinho.html")
