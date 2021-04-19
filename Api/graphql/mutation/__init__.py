from graphene import ObjectType

from .generos import GenerosMutation, RemoveGenero
from .permissions import (UserPermissionsMutation, GroupMutation, GroupPermissionMutation,
                          RemoveGroup, RemoveUserPermission, )
from .user import RemoveUser, UserSignUpMutation


class Mutation(ObjectType):
    genero = GenerosMutation.Field()
    user_signUp = UserSignUpMutation.Field()
    user_permissions = UserPermissionsMutation.Field()
    group = GroupMutation.Field()
    group_permissions = GroupPermissionMutation.Field()

    remove_genero = RemoveGenero.Field()
    remove_user = RemoveUser.Field()
    remove_user_permission = RemoveUserPermission.Field()
    remove_group = RemoveGroup.Field()
