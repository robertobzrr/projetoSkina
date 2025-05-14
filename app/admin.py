from django.contrib import admin
from .models import Categoria, Produtos, Lista, Lista_Produtos, Categoria_Produto


#admin.site.register(Categoria)
admin.site.register(Produtos)
admin.site.register(Lista)
admin.site.register(Lista_Produtos)
admin.site.register(Categoria_Produto)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('cod_cat', 'nome', 'hash_value')
    readonly_fields = ('hash_value',) 

