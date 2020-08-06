from django import forms
from .models import Equipamentos, Cliente

class FormEquipamento(forms.ModelForm):

    class Meta():
        model = Equipamentos
        fields = '__all__'


class FormCliente(forms.ModelForm):

    class Meta():
        model = Cliente
        exclude = ['id_equipamentos']
