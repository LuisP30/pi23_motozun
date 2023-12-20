from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def solicitacao(request):
    return render(request, 'solicitacao.html')

def cadastro(request):
    return render (request, 'cadastro00.html')