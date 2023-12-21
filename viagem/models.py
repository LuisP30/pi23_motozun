from django.db import models

class Viagem(models.Model):
    id= models.CharField 

class mototaxi(models.Model):
    nome = models.CharField('nome', max_length=120)
    cpf = models.CharField('cpf', max_length=12)
    data_nascimento= models.DateField('data_nascimento')
    cnh= models.CharField('cnh', max_length=9)
    placa= models.CharField('Placa', max_length=7)
    marca= models.CharField('montadora', max_length=15)
    modelo= models.CharField('modelo', max_length=15)