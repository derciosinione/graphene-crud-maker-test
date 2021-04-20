from django.db import models
from uuid import uuid4


class Generos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)   
    designacao = models.CharField(db_column='Designacao', max_length=100, blank=True, null=True)   
    datacriacao = models.DateTimeField(db_column='DataCriacao', auto_now_add=True, blank=True, null=True)   
    dataatualizacao = models.DateTimeField(db_column='DataAtualizacao',auto_now=True, blank=True, null=True)   

    class Meta:
        db_table = 'Generos'
