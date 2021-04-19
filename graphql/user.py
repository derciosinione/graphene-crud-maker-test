from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import user
    

class userType(DjangoObjectType):
    class Meta:
        model = user
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)