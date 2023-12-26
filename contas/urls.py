from django.urls import path
from contas.views import login_view, register_view, logout_view



urlpatterns = [
    path('login/', login_view, name='login'),
    path('cadastro/',register_view, name='cadastro'),
    path('sair/', logout_view, name='sair'),
    

   




]