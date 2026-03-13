from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuarios/", include("usuarios.urls")),
    path("carrinho/", include("carrinho.urls")),
    path("", include("produtos.urls")),
]
