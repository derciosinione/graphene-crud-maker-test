from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import Paises


class PaisesType(DjangoObjectType):
    class Meta:
        model = Paises
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)
