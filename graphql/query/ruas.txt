from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import ruas
    

class ruasType(DjangoObjectType):
    class Meta:
        model = ruas
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)