from django.db import models

# Create your models here.
class Equipamentos(models.Model):
    nome = models.CharField(max_length=150)
    layout = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    ip = models.CharField(max_length=30)
    hostname = models.CharField(max_length=150)
    morada = models.CharField(max_length=150)
    id_equipamentos = models.ForeignKey(Equipamentos, on_delete=models.CASCADE)
