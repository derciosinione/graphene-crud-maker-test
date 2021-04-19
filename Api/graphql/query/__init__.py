from graphene_django.filter import DjangoFilterConnectionField
from graphene import ObjectType

from Core.utils import CustomNode

from .generos import GenerosType
from .user import UserType
from .permissions import *


class Query(ObjectType):
    genero = CustomNode.Field(GenerosType)
    all_genero = DjangoFilterConnectionField(GenerosType)
   
    user = CustomNode.Field(UserType)
    all_users = DjangoFilterConnectionField(UserType)

    user_permission = CustomNode.Field(User_permissionsType)
    all_user_permissions = DjangoFilterConnectionField(User_permissionsType)

    permission = CustomNode.Field(PermissionsType)
    all_permissions = DjangoFilterConnectionField(PermissionsType)

    group = CustomNode.Field(GroupType)
    all_groups = DjangoFilterConnectionField(GroupType)
    