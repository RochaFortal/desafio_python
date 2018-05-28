from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_movimentacao(sender, **kwargs):
    from .models import Movimentacao
    Movimentacao.objects.bulk_create([
        Movimentacao(tipo='Entrada'),
        Movimentacao(tipo='Saída')
    ])


class LojaConfig(AppConfig):
    name = 'loja'

    def ready(self):
        post_migrate.connect(create_movimentacao, sender=self)
