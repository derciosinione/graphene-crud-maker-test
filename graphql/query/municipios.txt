from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import municipios
    

class municipiosType(DjangoObjectType):
    class Meta:
        model = municipios
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)