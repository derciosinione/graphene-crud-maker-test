from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import Provincias


class ProvinciasType(DjangoObjectType):
    class Meta:
        model = Provincias
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
