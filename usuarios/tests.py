from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Cliente


class ClienteModelTest(TestCase):
    def test_cliente_creation_on_user_create(self):
        """Testa se o perfil de Cliente é criado automaticamente via Signal."""
        user = User.objects.create_user(username="testuser", password="StrongPassword123!")
        self.assertTrue(Cliente.objects.filter(user=user).exists())
        self.assertEqual(str(user.cliente), "testuser - Sem CPF")


class UsuariosViewsTest(TestCase):
    def setUp(self):
        self.cadastrar_url = reverse("usuarios:cadastrar")
        self.login_url = reverse("usuarios:login")
        self.perfil_url = reverse("usuarios:perfil")
        self.user_data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "first_name": "New",
            "last_name": "User",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
        }

    def test_cadastrar_view_get(self):
        """Testa se a página de cadastro carrega corretamente."""
        response = self.client.get(self.cadastrar_url)
        self.assertEqual(response.status_code, 200)

    def test_cadastrar_view_post_valid(self):
        """Testa se o cadastro de um novo usuário funciona."""
        response = self.client.post(self.cadastrar_url, self.user_data)
        # Verifica se o usuário foi criado (contando 1 pois o banco de testes é limpo a cada teste)
        self.assertEqual(User.objects.filter(username="newuser").count(), 1)
        self.assertRedirects(response, self.perfil_url)

    def test_perfil_view_requires_login(self):
        """Testa se o perfil exige login para ser acessado."""
        response = self.client.get(self.perfil_url)
        # O Django redireciona para a LOGIN_URL que definimos no settings
        # O reverse de 'usuarios:login' gera '/usuarios/login/'
        expected_url = f"{self.login_url}?next={self.perfil_url}"
        self.assertRedirects(response, expected_url)

    def test_perfil_view_authenticated_get(self):
        """Testa se usuário logado acessa o perfil."""
        User.objects.create_user(username="member", password="StrongPassword123!")
        self.client.login(username="member", password="StrongPassword123!")
        response = self.client.get(self.perfil_url)
        self.assertEqual(response.status_code, 200)

    def test_perfil_update_post(self):
        """Testa a atualização dos dados do perfil."""
        user = User.objects.create_user(username="member", password="StrongPassword123!")
        self.client.login(username="member", password="StrongPassword123!")
        
        update_data = {
            "cpf": "98765432100",
            "telefone": "11999999999",
            "endereco": "Rua dos Doces, 123",
            "data_nascimento": "1990-01-01",
        }
        response = self.client.post(self.perfil_url, update_data)
        user.cliente.refresh_from_db()
        
        self.assertEqual(user.cliente.cpf, "98765432100")
        self.assertRedirects(response, self.perfil_url)
