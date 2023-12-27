from django.urls import path
from django.contrib import admin
from .views import *
from viagem.views import *
from django.contrib.auth.views import LoginView

app_name = 'viagem'

urlpatterns = [
    path('', solicitacao_viagem, name='solicitacao_viagem'), # URL em que o passageiro faz a solicitação
    path('mototaxista-solicitacoes/', mototaxista_aceite, name='mototaxista-solicitacoes'), # URL em que o Mototaxista ver as solicitações
    path('tela-viagem/<int:id>', tela_viagem, name='tela_viagem'), # URL em que passageiro e mototaxista são redirecionados quando possuem uma viagem em andamento
]
