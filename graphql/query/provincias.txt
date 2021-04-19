from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import provincias
    

class provinciasType(DjangoObjectType):
    class Meta:
        model = provincias
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)