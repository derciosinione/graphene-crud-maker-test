from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import Municipios
# derone Api Municipios

class MunicipiosType(DjangoObjectType):
    class Meta:
        model = Municipios
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
