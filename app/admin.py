from django.contrib import admin
from .models import Categoria, Produto, Categoria_Produto


admin.site.register(Categoria)
admin.site.register(Produto)
# admin.site.register(Lista)
# admin.site.register(Lista_Produtos)
admin.site.register(Categoria_Produto)


