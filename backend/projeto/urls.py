from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import home, CategoriaViewSet, ProdutosViewSet, ListaViewSet, Categoria_ProdutoViewSet, Lista_ProdutosViewSet


router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'produtos', ProdutosViewSet)
router.register(r'lista', ListaViewSet)
router.register(r'categoria_produto', Categoria_ProdutoViewSet)
router.register(r'lista_produtos', Lista_ProdutosViewSet)



urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
