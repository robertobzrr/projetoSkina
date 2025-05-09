from django_filters import rest_framework as filters
from .models import Categoria, Produtos, Lista, Lista_Produtos, Categoria_Produto


class CategoriaFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['nome']




class ProdutosFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Produtos
        fields = ['nome']




class ListaFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Lista
        fields = ['nome']




class Lista_ProdutosFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Lista_Produtos
        fields = ['cod_prod', 'cod_list']




class Categoria_ProdutoFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria_Produto
        fields = ['cod_cat', 'cod_prod']