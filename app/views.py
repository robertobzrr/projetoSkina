from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Produtos, Lista, Categoria_Produto, Lista_Produtos
from .serializers import CategoriaSerializer, ProdutosSerializer, ListaSerializer, Categoria_ProdutoSerializer, Lista_ProdutosSerializer
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1> OF THE KING OF THE POWER</h1>")


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer


class ListaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer


class Categoria_ProdutoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria_Produto.objects.all()
    serializer_class = Categoria_ProdutoSerializer


class Lista_ProdutosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lista_Produtos.objects.all()
    serializer_class = Lista_ProdutosSerializer

