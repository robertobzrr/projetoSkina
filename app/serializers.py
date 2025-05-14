from rest_framework import serializers
from .models import Categoria, Produtos, Lista, Categoria_Produto, Lista_Produtos


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = '__all__'


class Categoria_ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_Produto
        fields = '__all__'


class Lista_ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista_Produtos
        fields = '__all__'


