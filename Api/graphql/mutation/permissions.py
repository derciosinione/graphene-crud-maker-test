from django.contrib.auth.models import Group
from graphql_jwt.decorators import permission_required

from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import User_permissions
from Api.graphql.query import User_permissionsType, GroupType


class UserPermissionsForm(forms.ModelForm):
    class Meta:
        model = User_permissions
        fields = ('user', 'permission',)


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)


class GroupPermissionForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('id',)


class UserPermissionsMutation(DjangoModelFormMutation):
    class Meta:
        form_class = UserPermissionsForm

    data = Field(User_permissionsType)

    @permission_required('Api.add_user_permissions')
    @permission_required('Api.change_user_permissions')
    def perform_mutate(form, info):
        #form.instance.userCreator = info.context.user

        data = form.save()
        return UserPermissionsMutation(data=data)


class GroupMutation(DjangoModelFormMutation):
    class Meta:
        form_class = GroupForm

    data = Field(GroupType)

    @permission_required('Api.add_group')
    @permission_required('Api.change_group')
    def perform_mutate(form, info):
        data = form.save()
        return GroupMutation(data=data)


class GroupPermissionMutation(Mutation):
    class Arguments:
        id = ID(required=True)
        permission_id = ID(required=True)

    data = Field(GroupType)

    def mutate(self, info, id, permission_id):
        try:
            print(id)
            print(permission_id)
            data = Group.objects.get(pk=id)
            return GroupPermissionMutation(data=data)
        except Group.DoesNotExis:
            return None


class RemoveUserPermission(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    @permission_required('auth.delete_user_permissions')
    def mutate(self, info, id):
        try:  
            obj = User_permissions.objects.get(pk=id)
            obj.delete()
            return RemoveUserPermission(deleted=True)
        except User_permissions.DoesNotExis:
            return None

class RemoveGroup(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    @permission_required('auth.delete_user_permissions')
    def mutate(self, info, id):
        try:
            obj = Group.objects.get(pk=id)
            obj.delete()
            return RemoveGroup(deleted=True)
        except Group.DoesNotExis:
            return None
