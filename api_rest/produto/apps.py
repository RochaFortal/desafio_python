from django.apps import AppConfig
from django.db.models.signals import post_migrate
#from produto.signals import create_categoria

def create_categoria(sender, **kwargs):
    from produto.models import Categoria
    Categoria.objects.bulk_create([
        Categoria(nome='Placa de Vídeo'),
        Categoria(nome='Processador'),
        Categoria(nome='Disco Rígido'),
        Categoria(nome='Memória'),
        Categoria(nome='Placa Mãe'),
        Categoria(nome='Gabinete'),
        Categoria(nome='Fonte'),
    ])


class ProdutoConfig(AppConfig):
    name = 'produto'

    def ready(self):
        post_migrate.connect(create_categoria, sender=self)
