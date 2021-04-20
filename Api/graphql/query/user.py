from graphene_django import DjangoObjectType
from graphene import String

from Core.utils import CustomNode
from Api.models import User


# *------------------ QUERIES SECTION *-------------------
class UserType(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
        }
        exclude = ('password',)
        interfaces = (CustomNode,)

    full_name = String()

    def resolve_full_name(self, info):
        return '%s %s' % (self.first_name, self.last_name)

