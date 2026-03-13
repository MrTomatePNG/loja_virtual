from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente


class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True, label="Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("cpf", "telefone", "endereco", "data_nascimento")
        widgets = {
            "data_nascimento": forms.DateInput(attrs={"type": "date"}),
            "endereco": forms.Textarea(attrs={"rows": 3}),
        }
