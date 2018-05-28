from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False, unique=True)


class Produto(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField()
    valor = models.DecimalField(decimal_places=2, max_digits=11)
    categoria = models.OneToOneField(Categoria)