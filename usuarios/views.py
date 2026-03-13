from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CadastroForm, ClienteForm


def cadastrar(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático após cadastro bem-sucedido
            messages.success(
                request, f"Bem-vindo(a), {user.first_name}! Sua conta foi criada."
            )
            return redirect("usuarios:perfil")
    else:
        form = CadastroForm()
    return render(request, "usuarios/cadastrar.html", {"form": form})


@login_required
def perfil(request):
    # O user.cliente é garantido pelo Signal
    cliente = request.user.cliente

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("usuarios:perfil")
    else:
        form = ClienteForm(instance=cliente)

    return render(request, "usuarios/perfil.html", {"form": form})
