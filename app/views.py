from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria
from .serializers import CategoriaSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> OF THE KING OF THE POWER</h1>")


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer