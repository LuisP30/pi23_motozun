from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MyUserManager (BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, null=True)
    contato = models.CharField(max_length=11, null=True)
    disponibilidade = models.BooleanField(null=True, default = False)
    imagem = models.ImageField(null = True, upload_to='users-img')
    #verifica se o usuario está ativo ou não.
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField('date joined', null=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    objects = MyUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_short_name(self):
        return self.first_name
