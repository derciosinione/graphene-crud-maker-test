from graphene_django import DjangoObjectType
from django.contrib.auth.models import Permission, Group

from Core.utils import CustomNode

from Api.models import User_permissions


class User_permissionsType(DjangoObjectType):
    class Meta:
        model = User_permissions
        filter_fields = {
            'user': ['exact', ],
            'permission': ['exact', ],
        }
        interfaces = (CustomNode,)


class PermissionsType(DjangoObjectType):
    class Meta:
        model = Permission
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'codename': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (CustomNode,)


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (CustomNode,)


