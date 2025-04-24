from django.contrib import admin
from .models import Categoria, Produtos, Lista, Lista_Produtos, Categoria_Produto


admin.site.register(Categoria)
admin.site.register(Produtos)
admin.site.register(Lista)
admin.site.register(Lista_Produtos)
admin.site.register(Categoria_Produto)

