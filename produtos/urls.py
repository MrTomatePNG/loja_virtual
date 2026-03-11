from django.urls import path

from produtos import views

urlpatterns = [
    path("", views.listar_produtos, name="lista-produtos"),
    path("detalhes/<slug:slug>/", views.detalhes, name="detalhes-produto"),
]
