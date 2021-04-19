from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import bairros
    

class bairrosType(DjangoObjectType):
    class Meta:
        model = bairros
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)