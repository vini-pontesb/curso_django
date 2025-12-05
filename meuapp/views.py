from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    nome = 'Vinicius'
    return render(request, 'home.html', {'nome':nome})

def mensagem(request):
    nome = 'Vinicius'
    horario = datetime.now().hour

    if 5 <= horario < 12:
        mensagem = f'Bom dia!'
    elif 12 <= horario < 18:
        mensagem = f'Boa tarde!'
    else:
        mensagem = f'Boa noite!'
    return render(request, 'home.html', {'mensagem':mensagem, 'nome':nome})

def saudacao(resquest, nome):
    mensagem = f'Olá {nome}, seja bem vindx ao meu site!'
    return HttpResponse(mensagem)

def produtos(request, id_produto):
    produtos = {
        1: 'Notebook',
        2: 'Mouse',
        3: 'Fone'
    }
    produto = produtos.get(id_produto)
    if produto is None:
        mensagem = f'O produto não existe'
        return HttpResponse(mensagem)
    else:
        mensagem = f'Detalhes do produto: {produto}'
        return HttpResponse(mensagem)

def produtos2(request):
    produtos = ['Notebook', 'Mouse', 'Fone', 'Mouse', 'Celular']
    return render(produtos, 'produtos.hmtl', {'produtos':produtos})