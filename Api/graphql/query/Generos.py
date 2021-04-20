from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import Generos


class GenerosType(DjangoObjectType):
    class Meta:
        model = Generos
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)
