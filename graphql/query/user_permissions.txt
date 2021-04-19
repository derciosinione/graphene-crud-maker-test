from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import user_permissions
    

class user_permissionsType(DjangoObjectType):
    class Meta:
        model = user_permissions
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)