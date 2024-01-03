from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from rolepermissions.roles import assign_role, get_user_roles
from pi23_motozun import roles


def home(request):
    # assign_role(request.user, roles.Mototaxista)
    if request.user.groups.filter(name='mototaxista').exists():
        mototaxista = MyUser.objects.filter(id=request.user.id).get()
        viagem_em_andamento = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Mototaxista_Aceite.objects.filter(mototaxista=mototaxista, aceite=True).values('solicitacao'))
        if viagem_em_andamento:
            return redirect('')
    return render(request, 'index.html')

def solicitacao_viagem(request):
    if request.user.is_authenticated is False:
        return redirect('login')
    if request.user.groups.filter(name='mototaxista').exists():
        mototaxista = MyUser.objects.filter(id=request.user.id).get()
        viagem_em_andamento = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Mototaxista_Aceite.objects.filter(mototaxista=mototaxista, aceite=True).values('solicitacao'))
        if viagem_em_andamento:
            return redirect('')
    # if request.POST:
    #     passageiro = MyUser.objects.filter(id = request.user.id)
    #     ponto_partida = request.POST["ponto_partida"]
    #     ponto_destino = request.POST["ponto_destino"]
    #     solicitacao = Solicitacao(
    #         passageiro = passageiro,
    #         ponto_partida = ponto_partida,
    #         ponto_destino = ponto_destino
    #     )
    #     solicitacao.save()
    return render(request, 'solicitacao.html')

def muda_disponibilidade(request, id):
    usuario = MyUser.objects.filter(id=id).get()
    if usuario.disponibilidade is False:
        usuario.disponibilidade = True
    else:
        usuario.disponibilidade = False
    usuario.save()
    return redirect('viagem:solicitacao_viagem')

def tela_viagem(request, id):
    mototaxista_id = request.user.id
    solicitacao = Solicitacao.objects.filter(id=id)
    mototaxista = mototaxista.objects.filter(id = mototaxista_id)
    mototaxista_aceite = mototaxista(
        solicitacao = solicitacao,
        mototaxista = mototaxista,
        aceite = True
    )
    return render(request, 'tela-viagem.html', context={
        'solicitacao': solicitacao
    })

def cadastro(request):
    return render (request, 'cadastro00.html')


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

