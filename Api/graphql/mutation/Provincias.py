from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import Provincias
from Api.graphql.query import ProvinciasType


class ProvinciasForm(forms.ModelForm):
    class Meta:
        model = Provincias
        fields = ['codprovincia', 'nome', 'paisid']


class ProvinciasMutation(DjangoModelFormMutation):
    class Meta:
        form_class = ProvinciasForm

    data = Field(ProvinciasType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return ProvinciasMutation(data=data)
        except form.DoesNotExis:
            return None


class RemoveProvincias(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    def mutate(self, info, id):
        try:
            obj = Provincias.objects.get(pk=id)
            obj.delete()
            return RemoveProvincias(deleted=True)
        except Provincias.DoesNotExist:
            return None
