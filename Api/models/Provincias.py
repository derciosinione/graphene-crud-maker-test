from django.db import models
from uuid import uuid4
from .Paises import Paises


class Provincias(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(db_column="Nome", max_length=100, blank=True, null=True)
    paisid = models.ForeignKey(Paises,models.DO_NOTHING,db_column="PaisId", blank=True, null=True)
    codprovincia = models.CharField(db_column="CodProvincia", max_length=50, blank=True, null=True)
    datacriacao = models.DateTimeField(db_column="DataCriacao", blank=True, null=True)
    dataatualizacao = models.DateTimeField(db_column="DataAtualizacao", blank=True, null=True)

    class Meta:
        db_table="Provincias"