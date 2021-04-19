# field_name = [field.name for field in Generos._meta.get_fields()]
# field_name.remove('id')


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
