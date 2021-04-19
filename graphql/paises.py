from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import paises
    

class paisesType(DjangoObjectType):
    class Meta:
        model = paises
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)