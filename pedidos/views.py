from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from carrinho.cart import Carrinho

from .models import ItemPedido, Pedido


@login_required
def checkout(request):
    """Lógica para transformar o carrinho em um pedido real."""
    carrinho = Carrinho(request)

    if len(carrinho) == 0:
        messages.error(request, "Seu carrinho está vazio.")
        return redirect("produtos:lista-produtos")

    # Verifica se o cliente tem endereço cadastrado no perfil
    cliente = getattr(request.user, "cliente", None)
    if not cliente or not cliente.endereco:
        messages.warning(
            request,
            "Por favor, complete seu endereço no perfil antes de fechar o pedido.",
        )
        return redirect("usuarios:perfil")

    if request.method == "POST":
        # Cria o pedido no banco
        pedido = Pedido.objects.create(
            usuario=request.user,
            endereco_entrega=cliente.endereco,
        )

        # Transfere os itens do carrinho para o pedido
        for item in carrinho:
            ItemPedido.objects.create(
                pedido=pedido,
                produto_variacao=item["produto_variacao"],
                preco=item["preco"],
                quantidade=item["quantidade"],
            )
            # Aqui poderíamos diminuir o estoque real se quiséssemos
            variacao = item["produto_variacao"]
            if variacao.estoque >= item["quantidade"]:
                variacao.estoque -= item["quantidade"]
                variacao.save()

        # Limpa o carrinho da sessão
        carrinho.limpar()

        return render(request, "pedidos/sucesso.html", {"pedido": pedido})

    # Se for GET, apenas mostra a página de confirmação
    return render(
        request, "pedidos/confirmar.html", {"carrinho": carrinho, "cliente": cliente}
    )


@login_required
def meus_pedidos(request):
    """Lista o histórico de compras do cliente (O 'Read' do CRUD)."""
    pedidos = request.user.pedidos.all()
    return render(request, "pedidos/lista.html", {"pedidos": pedidos})
