from django.urls import path
from app.views import categoria_lista, catergoria_criando

urlpatterns = [
    path('categoria_lista/', categoria_lista, name="categorialista"),
    path('categoria_criando/', catergoria_criando),
]