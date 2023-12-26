from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    return render(request, 'index.html')

def solicitacao(request):
    return render(request, 'solicitacao.html')

def cadastro(request):
    return render (request, 'cadastro00.html')

def perfil(request):
    return render (request, 'perfil.html')

#_________ CRUD MOTOTAXI ______
def cadastromoto(request):
    form = mototaxiform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cadastro')
    
    contexto = {
        'form_mototaxi':form
    }
    return render (request, 'cadastro_mototaxi.html', contexto)
