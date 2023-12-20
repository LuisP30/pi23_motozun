from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .custom_manager import CustomUserManager

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField('Nome', max_length=75, blank=False, null=False)
    sobrenome = models.CharField('Sobrenome', max_length=45, blank=False, null=False)
    email = models.EmailField('E-mail', max_length=100, blank=False, null=False, unique=True)
    cpf = models.CharField('CPF', max_length=11, blank=False, null=False, unique=True)
    contato = models.CharField('Contato', max_length=15, blank=False, null=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('nome', 'sobrenome', 'cpf', 'password',)

    def __str__(self):
        return str(self.id)
        


class Mototaxista(models.Model):
    imagem = models.ImageField('Imagem', upload_to='users-img')
    disponivel = models.BooleanField('Disponivel', null=False, default=False)
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)

class Passageiro(models.Model):
    endereco = models.CharField('Endereço', max_length=15, blank=False, null=False)
    usuario = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
