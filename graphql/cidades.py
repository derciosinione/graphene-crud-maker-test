from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import cidades
    

class cidadesType(DjangoObjectType):
    class Meta:
        model = cidades
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)