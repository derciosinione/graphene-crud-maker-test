from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import Cidades


class CidadesType(DjangoObjectType):
    class Meta:
        model = Cidades
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)
