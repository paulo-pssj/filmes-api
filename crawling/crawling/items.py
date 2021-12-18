import scrapy
from scrapy_djangoitem import DjangoItem
from filme.models import Filme

class FilmeItem(DjangoItem):
    django_model = Filme
    
