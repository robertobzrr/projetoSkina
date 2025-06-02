from django_filters import rest_framework as filters
from .models import Categoria, Produto, Categoria_Produto


class CategoriaFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['nome']



class ProdutoFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Produto
        fields = ['nome']



class Categoria_ProdutoFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria_Produto
        fields = ['nome', 'categoria', 'produto']


# class ListaFilter(filters.FilterSet):
#     nome = filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = Lista
#         fields = ['nome']




# class Lista_ProdutosFilter(filters.FilterSet):
#     nome = filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = Lista_Produtos
#         fields = ['nome', 'cod_prod', 'cod_list']




