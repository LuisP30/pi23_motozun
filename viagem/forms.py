from django.forms import ModelForm
from .models import mototaxi

class mototaxiform(ModelForm):
    class Meta:
        model = mototaxi
        fields = ['nome','cpf','data_nascimento','cnh','placa','marca','modelo']