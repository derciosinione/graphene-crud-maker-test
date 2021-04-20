from django.db import models
from uuid import uuid4
from .Provincias import Provincias

class Municipios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(db_column="Nome", max_length=100, blank=True, null=True)
    provinciaid = models.ForeignKey(Provincias,models.DO_NOTHING,db_column="ProvinciaId", blank=True, null=True)
    codmunicipio = models.CharField(db_column="CodMunicipio", max_length=50, blank=True, null=True)
    datacriacao = models.DateTimeField(db_column="DataCriacao", blank=True, null=True)
    dataatualizacao = models.DateTimeField(db_column="DataAtualizacao", blank=True, null=True)

    class Meta:
        db_table="Municipios"