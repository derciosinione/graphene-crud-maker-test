from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import User_permissions
from Api.graphql.query import User_permissionsType


class User_permissionsForm(forms.ModelForm):
    class Meta:
        model = User_permissions
        fields = ['permission', 'user']


class User_permissionsMutation(DjangoModelFormMutation):
    class Meta:
        form_class = User_permissionsForm

    data = Field(User_permissionsType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return User_permissionsMutation(data=data)
        except form.DoesNotExis:
            return None


class RemoveUser_permissions(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    def mutate(self, info, id):
        try:
            obj = User_permissions.objects.get(pk=id)
            obj.delete()
            return RemoveUser_permissions(deleted=True)
        except User_permissions.DoesNotExist:
            return None
