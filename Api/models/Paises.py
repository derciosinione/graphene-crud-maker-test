from django.db import models
from uuid import uuid4

class Paises(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(db_column="Nome", max_length=100, blank=True, null=True)
    codigopais = models.CharField(db_column="CodigoPais", max_length=5, blank=True, null=True)
    ddd = models.CharField(db_column="DDI", max_length=5, blank=True, null=True)
    codpais = models.CharField(db_column="CodPais", max_length=50, blank=True, null=True)
    datacriacao = models.DateTimeField(db_column="DataCriacao", blank=True, null=True)
    dataatualizacao = models.DateTimeField(db_column="DataAtualizacao", blank=True, null=True)

    class Meta:
        db_table="Paises"