from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from rolepermissions.roles import assign_role
from pi23_motozun import roles
from contas import models

def home(request):
    # assign_role(request.user, roles.Mototaxista_Role)
    if request.user.groups.filter(name='mototaxista_role').exists():
        mototaxista = Mototaxista.objects.filter(usuario_id=request.user.id).get()
        print(mototaxista)
        mototaxista_aceitou_solicitacao = Mototaxista_Aceite.objects.filter(mototaxista = mototaxista, aceite = True).get()
        print(mototaxista_aceitou_solicitacao)

        return HttpResponse('Está funcionando')
    return render(request, 'index.html')

def solicitacao_viagem(request):
    
    conclusao_viagem = Conclusao_Viagem.objects.filter(concluido = False).get()
    # conclusao_viagem.solicitacao.passageiro.usuario.id
    if conclusao_viagem is not None:
        return redirect()
    if request.POST:
        user_id = request.user.id
        passageiro = Passageiro.objects.filter(id = user_id)
        ponto_partida = request.POST["ponto_partida"]
        ponto_destino = request.POST["ponto_destino"]
        solicitacao = Solicitacao(
            passageiro = passageiro,
            ponto_partida = ponto_partida,
            ponto_destino = ponto_destino
        )
        solicitacao.save()
    return render(request, 'solicitacao-passageiro.html')


def mototaxista_aceite(request):
    solicitacoes = Solicitacao.objects.filter()
    # if request.POST:
    #     mototaxista_aceitou = Mototaxista_Aceite(
    #         solicitacao = Solicitacao.objects.filter(id = id_solicitacao),
    #         mototaxista = Mototaxista.objects.filter(id = id_mototaxista),
    #     )
    #     if request.POST['aceite'] is True:
    #         mototaxista_aceitou.save()
    #         return redirect('viagem:tela_viagem')
    return render(request, 'solicitacao-mototaxista.html', context={
        'solicitacoes': solicitacoes,
    })

def tela_viagem(request, id):
    mototaxista_id = request.user.id
    solicitacao = Solicitacao.objects.filter(id=id)
    mototaxista = Mototaxista.objects.filter(id = mototaxista_id)
    mototaxista_aceite = Mototaxista(
        solicitacao = solicitacao,
        mototaxista = mototaxista,
        aceite = True
    )
    return render(request, 'tela-viagem.html', context={
        'solicitacao': solicitacao
    })

def cadastro(request):
    return render (request, 'cadastro00.html')

def perfil(request):

    listar_dados = models.MyUser.objects.all()
    contexto = {
        'listar_dados': listar_dados
    }
    return render (request, 'perfil.html', contexto)

#_________ CRUD MOTOTAXI ______
# def cadastromoto(request):
#     form = mototaxiform(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('cadastro')
    
#     contexto = {
#         'form_mototaxi':form
#     }
#     return render (request, 'cadastro_mototaxi.html', contexto)

