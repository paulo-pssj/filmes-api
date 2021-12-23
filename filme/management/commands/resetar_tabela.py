from django.core.management.base import BaseCommand, CommandError
from filme.models import Filme

class Command(BaseCommand):
    help = 'Deleta todos dados da tabala filme'
    
    def handle(self):
        try:
            Filme.objects.all().delete()
        
        except:
            raise CommandError('Erro ao deletar tabela')