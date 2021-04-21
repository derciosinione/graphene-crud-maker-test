from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import User_permissions
# derone Api User_permissions

class User_permissionsType(DjangoObjectType):
    class Meta:
        model = User_permissions
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
