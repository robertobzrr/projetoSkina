from django.db import models
import hashlib



class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Produto(models.Model):
    nome = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return self.nome



class Categoria_Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column="cod_cat")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, db_column="cod_prod")
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["categoria", "produto"], name="Categoria_Produto_CompositePrimaryKey")
        ]





# class Lista(models.Model):
#     cod_list = models.IntegerField(primary_key=True)
#     nome = models.CharField(max_length=100)
#    # produtos = models.ManyToManyField(Produtos, through="Lista_produtos")

#     def __str__(self):
#         return self.nome



# class Lista_Produtos(models.Model):
#     cod_prod = models.ForeignKey(Produtos, on_delete=models.CASCADE, db_column="cod_prod")
#     cod_list = models.ForeignKey(Lista, on_delete=models.CASCADE, db_column="cod_list")
#     nome = models.CharField(max_length=100, blank=True)


#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=["cod_prod", "cod_list"], name="Lista_Produtos_CompositePrimaryKey")
#         ]
 