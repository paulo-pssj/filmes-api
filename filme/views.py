from rest_framework import viewsets
from filme.serializers import FilmeSerializer
from filme.models import Filme

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    http_method_names = ['get']
