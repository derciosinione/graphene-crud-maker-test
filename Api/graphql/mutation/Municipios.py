from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import Municipios
from Api.graphql.query import MunicipiosType


class MunicipiosForm(forms.ModelForm):
    class Meta:
        model = Municipios
        fields = ['codmunicipio', 'nome', 'provinciaid']


class MunicipiosMutation(DjangoModelFormMutation):
    class Meta:
        form_class = MunicipiosForm

    data = Field(MunicipiosType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return MunicipiosMutation(data=data)
        except form.DoesNotExis:
            return None


class RemoveMunicipios(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    def mutate(self, info, id):
        try:
            obj = Municipios.objects.get(pk=id)
            obj.delete()
            return RemoveMunicipios(deleted=True)
        except Municipios.DoesNotExist:
            return None
