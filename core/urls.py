from django.urls import path
from .views import *

urlpatterns = [
    path('solicitar/', solicitacao, name='solicitar')
]
