from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import User
# derone Api User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
