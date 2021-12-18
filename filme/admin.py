from django.contrib import admin
from .models import Filme

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'link')
    
admin.site.register(Filme, FilmeAdmin)
