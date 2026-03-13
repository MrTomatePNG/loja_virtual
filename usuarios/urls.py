from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("perfil/", views.perfil, name="perfil"),
    # Views integradas do Django
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="usuarios/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="produtos:listar_produtos"),
        name="logout",
    ),
]
