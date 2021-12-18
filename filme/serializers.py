from django.db.models import fields
from rest_framework import serializers
from filme.models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'sinopse', 'link']
    