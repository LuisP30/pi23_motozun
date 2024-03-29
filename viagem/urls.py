from django.urls import path
from django.contrib import admin
from .views import *
from viagem.views import *
from django.contrib.auth.views import LoginView

app_name = 'viagem'

urlpatterns = [
    path('', solicitacao_viagem, name='solicitacao_viagem'), # URL em que o passageiro faz a solicitação
    path('tela-viagem/<int:id>', tela_viagem, name='tela_viagem'), # URL em que passageiro e mototaxista são redirecionados quando possuem uma viagem em andamento
    path('disponibilidade/<int:id>', muda_disponibilidade, name='muda_disponibilidade'),
    path('aguardando-mototaxista/<int:id>', tela_espera, name='tela_espera'),
    path('viagem-aceita/<int:id>', mototaxista_aceitou_viagem, name='viagem_aceita'),
    path('viagem-concluida/<int:id>', mototaxista_concluiu_viagem, name='viagem_concluida'),
]
