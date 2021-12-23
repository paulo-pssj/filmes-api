from django.core.management.base import BaseCommand, CommandError
from filme.models import Filme

class Command(BaseCommand):
    help = 'Deleta todos dados da tabala filme'
    
    def add_arguments(self, parser):
        parser.add_argument('--drop-all', action='store_true', help=help)
        
    def handle(self, *args, **options):
        if options.get("drop_all"):
            self.warn("Apangando registros")
            Filme.objects.all().delete()
        
        