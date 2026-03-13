from django.urls import path

from .views import carrinho_view

urlpatterns = [
    path("carrinho/", carrinho_view, name="carrinho"),
]
