from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import Ruas


class RuasType(DjangoObjectType):
    class Meta:
        model = Ruas
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)
