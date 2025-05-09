from django.db import models
import hashlib





class Categoria(models.Model):
    cod_cat = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    hash_value = models.CharField(max_length=64, editable=False, blank=True)

    def save(self, *args, **kwargs):
        hash_input = f"{self.cod_cat}{self.nome}".encode('utf-8')
        self.hash_value = hashlib.sha256(hash_input).hexdigest()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.hash_value}"








class Produtos(models.Model):
    cod_prod = models.IntegerField(primary_key=True)
   # cod_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column="cod_cat")
    nome = models.CharField(max_length=100)
 

    def __str__(self):
        return self.nome







class Lista(models.Model):
    cod_list = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
   # produtos = models.ManyToManyField(Produtos, through="Lista_produtos")

    def __str__(self):
        return self.nome









class Lista_Produtos(models.Model):
    cod_prod = models.ForeignKey(Produtos, on_delete=models.CASCADE, db_column="cod_prod")
    cod_list = models.ForeignKey(Lista, on_delete=models.CASCADE, db_column="cod_list")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cod_prod", "cod_list"], name="Lista_Produtos_CompositePrimaryKey")
        ]
        





class Categoria_Produto(models.Model):
    cod_cat = models.ForeignKey(Categoria, on_delete=models.CASCADE, db_column="cod_cat")
    cod_prod = models.ForeignKey(Produtos, on_delete=models.CASCADE, db_column="cod_prod")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cod_cat", "cod_prod"], name="Categoria_Produto_CompositePrimaryKey")
        ]