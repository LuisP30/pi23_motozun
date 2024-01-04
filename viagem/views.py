from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist
import googlemaps

def home(request):
    return render(request, 'index.html')

def solicitacao_viagem(request):
    if request.user.is_authenticated is False:
        return redirect('login')
    usuario = MyUser.objects.filter(id=request.user.id).get()
    # Instruções de mototaxista:
    # Verificando grupo do usuário e se tem viagem em andamento
    if request.user.groups.filter(name='mototaxista').exists():
        viagem_em_andamento = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Mototaxista_Aceite.objects.filter(mototaxista=usuario, aceite=True).values('solicitacao'))
        if viagem_em_andamento:
            for viagem in viagem_em_andamento:               
                return redirect('viagem:tela_viagem', id=viagem.id)
        solicitacoes_aceitas = Mototaxista_Aceite.objects.values('solicitacao_id')
        solicitacoes_sem_aceite = Solicitacao.objects.exclude(id__in=solicitacoes_aceitas)

        return render(request, 'solicitacao.html', context={
            'solicitacoes': solicitacoes_sem_aceite,
        })
    # Instruções de passageiro:
    # Verificando grupo do usuário e se tem viagem em andamento
    elif request.user.groups.filter(name='passageiro').exists():
        # Verificando se passageiro possui viagem em andamento
        viagem_em_andamento = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Solicitacao.objects.filter(passageiro=usuario))
        if viagem_em_andamento:
            for viagem in viagem_em_andamento:
                if viagem:
                    return redirect('viagem:tela_viagem', id=viagem.solicitacao.id)
        # Verifica se tem solicitação em andamento
        solicitacoes_com_aceite_ids = Mototaxista_Aceite.objects.values('solicitacao_id')
        try:
            solicitacoes_sem_aceite = Solicitacao.objects.exclude(id__in=solicitacoes_com_aceite_ids).filter(passageiro=usuario).get()
        except ObjectDoesNotExist:
            solicitacoes_sem_aceite = None
        if solicitacoes_sem_aceite:
            if solicitacoes_sem_aceite.id != id:
                return redirect('viagem:tela_espera', id=solicitacoes_sem_aceite.id)
        if request.POST:
            ponto_partida = request.POST["partida"]
            ponto_destino = request.POST["destino"]
            solicitacao = Solicitacao(
                passageiro = usuario,
                ponto_partida = ponto_partida,
                ponto_destino = ponto_destino
            )
            solicitacao.save()
            print(solicitacao.id)
            return redirect('viagem:tela_espera', id=solicitacao.id)
    return render(request, 'solicitacao.html')

def muda_disponibilidade(request, id):
    if request.user.is_authenticated is True:
        usuario = MyUser.objects.filter(id=request.user.id).get()
    if usuario.disponibilidade is False:
        usuario.disponibilidade = True
    else:
        usuario.disponibilidade = False
    usuario.save()
    return redirect('viagem:solicitacao_viagem')

# Essa view é para passageiros
def tela_espera(request, id):
    # Verifica se tem viagem em andamento
    if request.user.is_authenticated is True:
        usuario = MyUser.objects.filter(id=request.user.id).get()
        viagem_em_andamento = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Solicitacao.objects.filter(passageiro=usuario))
        if viagem_em_andamento:
            for viagem in viagem_em_andamento:
                return redirect('viagem:tela_viagem', id=viagem.id)
        # Verifica se tem solicitação em andamento
        solicitacoes_com_aceite_ids = Mototaxista_Aceite.objects.values('solicitacao_id')
        try:
            solicitacoes_sem_aceite = Solicitacao.objects.exclude(id__in=solicitacoes_com_aceite_ids).filter(passageiro=usuario).get()
        except Solicitacao.DoesNotExist:
            solicitacoes_sem_aceite = None
        if solicitacoes_sem_aceite:
            if solicitacoes_sem_aceite.id != id:
                return redirect('viagem:tela_espera', id=solicitacoes_sem_aceite.id)
        solicitacao = Solicitacao.objects.filter(id=id)
        return render(request, 'tela_espera.html', context={
            'solicitacao': solicitacao,
        })
    else:
        return redirect('login')

def tela_viagem(request, id):
    usuario = MyUser.objects.filter(id=request.user.id).get()
    if request.user.groups.filter(name='mototaxista').exists():
        viagem_em_andamento = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Mototaxista_Aceite.objects.filter(mototaxista=usuario, aceite=True).values('solicitacao'))
        if viagem_em_andamento:
            for viagem in viagem_em_andamento:        
                if viagem.solicitacao.id != id:
                    return redirect('viagem:tela_viagem', id=viagem.solicitacao.id)
        else:
            return redirect('viagem:solicitacao_viagem')
    elif request.user.groups.filter(name='passageiro').exists():
        # Verifica se tem viagem em andamento
        viagem_em_andamento = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Solicitacao.objects.filter(passageiro=usuario))
        if viagem_em_andamento:
            for viagem in viagem_em_andamento:
                if viagem.solicitacao.id != id:
                    return redirect('viagem:tela_viagem', id=viagem.solicitacao.id)
        else:
            return redirect('viagem:solicitacao_viagem')
 
    solicitacao = Solicitacao.objects.filter(id=id)
    return render(request, 'tela-viagem.html', context={
        'solicitacoes': solicitacao
    })

def mototaxista_aceitou_viagem(request, id):
    if request.user.groups.filter(name='mototaxista').exists():
        usuario = MyUser.objects.filter(id=request.user.id).get()
        solicitacao = Solicitacao.objects.filter(id=id).get()
        moto_aceite = Mototaxista_Aceite(
            solicitacao = solicitacao,
            mototaxista = usuario,
            aceite = True
        )
        moto_aceite.save()
        viagem_concluida = Conclusao_Viagem(
            solicitacao = solicitacao,
            concluido = False,
            valor = 5
        )
        viagem_concluida.save()
    return redirect('viagem:tela_viagem', id=id)

def mototaxista_concluiu_viagem(request, id):
    usuario = MyUser.objects.filter(id=request.user.id).get()
    viagem_em_andamento = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Mototaxista_Aceite.objects.filter(mototaxista=usuario, aceite=True).values('solicitacao'))
    print(viagem_em_andamento)
    viagem = Conclusao_Viagem.objects.filter(concluido=False, solicitacao__in=Solicitacao.objects.filter(id=id)).get()
    print(viagem)
    viagem.concluido = True
    viagem.save()
    return redirect('viagem:solicitacao_viagem')