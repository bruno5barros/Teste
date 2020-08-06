from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.shortcuts import redirect
import json
from .forms import FormEquipamento, FormCliente


class home(ListView):
    context_object_name = 'clientes'
    model = Cliente
    template_name = 'home.html'


def GerarConfig(request):
    equipamentos = Equipamentos.objects.all()

    for equipamento in equipamentos:
        try:
            res = json.loads(equipamento.layout)
            print(res['nome'])
            cliente = Cliente.objects.get(id_equipamentos=equipamento)
            print(cliente)
            cliente.nome = res['nome']
            cliente.ip = res['ip']
            cliente.hostname = res['hostname']
            cliente.morada = res['morada']

            cliente.save()
        except:
            print("Erro na coluna layout")

    return redirect('home')


def equipamento_form(request):

    equipamento_form = FormEquipamento()
    cliente_form = FormCliente()

    if request.method == "POST":
        print("*********************** POST *******************************")
        equipamento_form = FormEquipamento(request.POST)
        cliente_form = FormCliente(request.POST)

        if equipamento_form.is_valid() and cliente_form.is_valid():
            equipamentos = equipamento_form.save(commit=True)
            cliente = cliente_form.save(commit=False)
            cliente.id_equipamentos = equipamentos
            cliente.save()
            print("Form submitido")

        else:
            print("Form invalido")

    return render(request, 'equipamento.html', {'form': equipamento_form, 'cliente_form': cliente_form})
