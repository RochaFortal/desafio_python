from django.db import models
from django.contrib.auth.models import User
from produto.models import Produto


class Pedido(models.Model):
    numero = models.IntegerField()
    user = models.OneToOneField(User)
    produtos = models.ManyToManyField(Produto)


class Movimentacao(models.Model):
    tipo = models.CharField(max_length=40)


class Estoque(models.Model):
    produto = models.OneToOneField(Produto)
    quantidade = models.IntegerField()
    tipo = models.OneToOneField(Movimentacao)
