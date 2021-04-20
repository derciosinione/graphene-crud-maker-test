from django.db import models
from uuid import uuid4
from .Bairros import Bairros

class Ruas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(db_column="Nome", max_length=100, blank=True, null=True)
    bairroid = models.ForeignKey(Bairros,models.DO_NOTHING,db_column="BairroId", blank=True, null=True)
    codrua = models.CharField(db_column="CodRua", max_length=50, blank=True, null=True)
    datacriacao = models.DateTimeField(db_column="DataCriacao", blank=True, null=True)
    dataatualizacao = models.DateTimeField(db_column="DataAtualizacao", blank=True, null=True)

    class Meta:
        db_table="Ruas"