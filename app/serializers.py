from rest_framework import serializers
from .models import Categoria, Produto, Categoria_Produto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class Categoria_ProdutoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    produto = serializers.StringRelatedField()

    class Meta:
        model = Categoria_Produto
        fields = ['id', 'categoria', 'produto']



# class ListaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lista
#         fields = '__all__'


# class Lista_ProdutosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lista_Produtos
#         fields = '__all__'


