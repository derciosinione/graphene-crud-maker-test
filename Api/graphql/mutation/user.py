from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphql_jwt.decorators import permission_required
from graphene_django.forms.mutation import DjangoModelFormMutation
from django.contrib.auth.forms import UserCreationForm

from Api.models import User
from Core.utils import user_verification

from Api.graphql.query import UserType


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        field = [field.name for field in User._meta.get_fields()]
        exclude_fields = ['id', 'data_atualizacao', 'user_permis', 'refresh_tokens', 'logentry']
        
        # Removing exclude_fields
        for item in exclude_fields:
            if field.__contains__(item):
                field.remove(item)        
        
        fields = field


class UserSignUpMutation(DjangoModelFormMutation):
    """
    This method is to Sign Up a new User.
    """

    class Meta:
        form_class = UserSignUpForm

    data = Field(UserType)

    def perform_mutate(form, info):
        try:
            if form.instance.pk:
                user_verification(form.instance, info.context.user)

            data = form.save()
            return UserSignUpMutation(data=data)
        except form.DoesNotExis:
            return None

class RemoveUser(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    @permission_required('auth.delete_user')
    def mutate(self, info, id):
        try:
            obj = User.objects.get(pk=id)
            obj.delete()
            return RemoveUser(deleted=True)
        except User.DoesNotExist:
            return None
