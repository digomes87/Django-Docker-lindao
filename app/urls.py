from django.urls import path
from app.views import categoria_lista, catergoria_criando, home

urlpatterns = [
    path('categoria_lista/', categoria_lista, name="categorialista"),
    path('categoria_criando/', catergoria_criando),
    path('', home, name="home"),
]