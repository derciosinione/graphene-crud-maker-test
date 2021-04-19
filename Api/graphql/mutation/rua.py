from Api.graphql.query import RuasType
from Api.models import Ruas
from django import forms
from graphene import ID, Boolean, Field, Mutation
from graphene_django.forms.mutation import DjangoModelFormMutation


class RuasForms(RuasType):
    class Meta:
        model = Ruas
        fields = ("nome", "CodRua")


class RuasMutation(DjangoModelFormMutation):
    class Meta:
        form_class = Ruas

    data = Field(RuasType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return RuasMutation(data=data)
        except form.DoesNotExis:
            return None


class RemoveRuas(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    # @permission_required('auth.delete_bancos')
    def mutate(self, info, id):
        try:
            obj = Ruas.objects.get(pk=id)
            obj.delete()
            return RemoveRuas(deleted=True)
        except Ruas.DoesNotExist:
            return None