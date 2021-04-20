from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import Paises
from Api.graphql.query import PaisesType


class PaisesForm(forms.ModelForm):
    class Meta:
        model = Paises
        fields = ['nome', 'codigopais', 'ddd', 'codpais']


class PaisesMutation(DjangoModelFormMutation):
    class Meta:
        form_class = PaisesForm

    data = Field(PaisesType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return PaisesMutation(data=data)
        except form.DoesNotExis:
            return None


class RemovePaises(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    def mutate(self, info, id):
        try:
            obj = Paises.objects.get(pk=id)
            obj.delete()
            return RemovePaises(deleted=True)
        except Paises.DoesNotExist:
            return None
