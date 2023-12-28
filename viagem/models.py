from django.db import models
from contas.models import MyUser

class Solicitacao(models.Model):
    passageiro = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    ponto_partida = models.CharField( 'Ponto de partida', max_length=100, null = False)
    ponto_destino = models.CharField( 'Ponto de destino', max_length=100, null = False)
    data_hora_solicitada = models.DateTimeField('Data e hora de solicitação', auto_now_add = True)

class Mototaxista_Aceite(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete = models.CASCADE)
    mototaxista = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    aceite = models.BooleanField( 'Confirmação de Mototaxista', null = True)
    data_hora_confirmada = models.DateTimeField('Data e hora de confirmação', auto_now_add = True)

class Conclusao_Viagem(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete = models.CASCADE)
    valor = models.DecimalField(null = False, max_digits=5, decimal_places=3)
    concluido = models.BooleanField( 'Viagem concluída', null = True)
    data_hora_corrida_iniciada = models.DateTimeField('Hora de início da corrida', auto_now_add = True)
    data_hora_corrida_finalizada = models.DateTimeField('Hora do fim da corrida', auto_now = True)
