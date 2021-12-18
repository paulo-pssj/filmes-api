from django.contrib import admin
from django.urls import path, include
from filme.views import FilmeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('filmes', FilmeViewSet, basename='filmes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
