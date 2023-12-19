from django.urls import path
from .views import *

app_name = 'viagem'

urlpatterns = [
    path('', solicitacao, name='solicitar')
]
