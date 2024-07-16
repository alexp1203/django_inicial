from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def ver_produto(request):
    if request.method =="GET":
        nome = 'Alex'
        return render(request, 'ver_produto.html', {'nome': nome})
    elif request.method =="POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        pessoa = Pessoa(nome=nome, idade=idade)

        pessoa.save()


        print(nome)
        return HttpResponse('Cadastro realizado com sucesso!')

def inserir_produto(request):
    return HttpResponse('Inserir produto')

