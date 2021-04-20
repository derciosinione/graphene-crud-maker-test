from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import User
from Api.graphql.query import UserType


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']


class UserMutation(DjangoModelFormMutation):
    class Meta:
        form_class = UserForm

    data = Field(UserType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return UserMutation(data=data)
        except form.DoesNotExis:
            return None


class RemoveUser(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    def mutate(self, info, id):
        try:
            obj = User.objects.get(pk=id)
            obj.delete()
            return RemoveUser(deleted=True)
        except User.DoesNotExist:
            return None
