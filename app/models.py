from django.db import models

class Categoria(models.Model):
    produto = models.CharField(max_length=255)
    descricao = models.TextField(null=True)
    esta_ativo = models.BooleanField(default=True)


    def __str__(self):
        return self.produto