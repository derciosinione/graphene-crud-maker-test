from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import generos
    

class generosType(DjangoObjectType):
    class Meta:
        model = generos
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)