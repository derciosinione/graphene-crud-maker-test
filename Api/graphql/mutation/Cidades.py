from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import Cidades
from Api.graphql.query import CidadesType


class CidadesForm(forms.ModelForm):
    class Meta:
        model = Cidades
        fields = ['nome', 'bairroid', 'codcidade']


class CidadesMutation(DjangoModelFormMutation):
    class Meta:
        form_class = CidadesForm

    data = Field(CidadesType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return CidadesMutation(data=data)
        except form.DoesNotExis:
            return None


class RemoveCidades(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    def mutate(self, info, id):
        try:
            obj = Cidades.objects.get(pk=id)
            obj.delete()
            return RemoveCidades(deleted=True)
        except Cidades.DoesNotExist:
            return None
