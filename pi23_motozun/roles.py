from rolepermissions.roles import AbstractUserRole

class Mototaxista(AbstractUserRole):
    available_permissions = {'ver_solicitacoes': True, 'concluir_viagem': True}

class Passageiro(AbstractUserRole):
    available_permissions = {'fazer_solicitacoes': True}

# ------- Como adicionar um usuário a um grupo : -------

# from rolepermissions.roles import assign_role
# assign_role(usuário, 'mototaxista_role') tem que passar dois parâmetros

# ------------ Permissões em nível de views ------------

# from rolepermissions.decorators import has_role_decorator, has_permission_decorator
# @has_role_decorator('passageiro_role')
# def solicitacao_viagem(request):
#   (essa é uma view apenas para passageiros acessarem)

# @has_permission_decorator('ver_solicitacoes')
# def solicitacoes(request):
#   (essa é uma view só pode ser acessada por usuários com a permissão ver_solicitacoes)
    
# ------------ Concedendo e revogando permissões ao usuário -----------

# from rolepermissions.permissions import grant_permission, revoke_permission
# revoke_permission(usuário, 'ver_solicitacoes') tem que passar dois parâmetros - Revogando
# grant_permission(usuário, 'ver_solicitacoes') tem que passar dois parâmetros - Concedendo

# ------------ Vendo permissões do usuário -----------

# from rolepermissions.roles import assign_role, get_user_roles
# print(get_user_roles(Usuário))

# ------------ Permissões em nível de template -----------

# {% permission_tags %}
# {% if user|has_role: 'mototaxista_role' %} Para grupos
# <h1>Página do Mototaxista </h1>
# {% endif %}

# {% if user|can: 'fazer_solicitacoes' %} Para permissões
# <h1>Página do Mototaxista </h1>
# {% endif %}