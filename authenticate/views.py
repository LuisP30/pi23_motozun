from django.shortcuts import render, redirect
from .models import Usuario


def perfil(request):

    listar_dados = Usuario.objects.all()
    contexto = {
        'listar_dados': listar_dados
    }
    return render (request, 'perfil.html', contexto)

def login(request):
    return render(request, 'login.html')
    

def cadastro(request):
    return render(request, 'cadastro.html')

