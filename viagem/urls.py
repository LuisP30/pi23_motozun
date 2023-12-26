from django.urls import path
from django.contrib import admin
from .views import *
from viagem.views import *
from django.contrib.auth.views import LoginView

app_name = 'viagem'

urlpatterns = [
    path('', solicitacao, name='solicitar'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastromoto/', cadastromoto, name='cadastro_mototaxi'),
    path('perfil/', perfil, name='perfil'),
]
