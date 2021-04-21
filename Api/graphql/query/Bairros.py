from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import Bairros


class BairrosType(DjangoObjectType):
    class Meta:
        model = Bairros
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
