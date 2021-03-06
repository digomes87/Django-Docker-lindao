from django.forms import ModelForm
from django.shortcuts import render, redirect

from app.models import Categoria

def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(request,'app/categoria_lista.html',{'categorias': categorias})


class CategoriaFormulario(ModelForm):
    class Meta:
        model = Categoria
        fields = ['name']


def catergoria_criando(request):
    form = CategoriaFormulario(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categorialista')

    return render(request, 'app/categoria_criando.html',{'form':form})