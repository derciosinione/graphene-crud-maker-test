from django.db import models
from uuid import uuid4


class Bairros(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(db_column="Nome", max_length=100, blank=True, null=True)
    cod_bairro = models.CharField(db_column="CodBairro", max_length=50, blank=True, null=True)
    data_criacao = models.DateTimeField(db_column="DataCriacao", blank=True, null=True)
    data_atualizacao = models.DateTimeField(db_column="DataAtualizacao", blank=True, null=True)

    class Meta:
        db_table="Bairros"