from produto.models import Categoria

def create_categoria():
    Categoria.objects.bulk_create([
        Categoria(nome='Placa de Vídeo'),
        Categoria(nome='Processador'),
        Categoria(nome='Disco Rígido'),
        Categoria(nome='Memória'),
        Categoria(nome='Placa Mãe'),
        Categoria(nome='Gabinete'),
        Categoria(nome='Fonte'),
    ])