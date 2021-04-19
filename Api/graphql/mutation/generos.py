from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import Generos
from Api.graphql.query import GenerosType


class GenerosForm(forms.ModelForm):
    class Meta:
        model = Generos
        fields = ('designacao',)


class GenerosMutation(DjangoModelFormMutation):
    class Meta:
        form_class = GenerosForm

    data = Field(GenerosType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return GenerosMutation(data=data)
        except form.DoesNotExis:
            return None


class RemoveGenero(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    # @permission_required('auth.delete_bancos')
    def mutate(self, info, id):
        try:
            obj = Generos.objects.get(pk=id)
            obj.delete()
            return RemoveGenero(deleted=True)
        except Generos.DoesNotExist:
            return None