from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import Bairros
from Api.graphql.query import BairrosType


class BairrosForm(forms.ModelForm):
    class Meta:
        model = Bairros
        fields = ['cod_bairro', 'nome']


class BairrosMutation(DjangoModelFormMutation):
    class Meta:
        form_class = BairrosForm

    data = Field(BairrosType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return BairrosMutation(data=data)
        except form.DoesNotExis:
            return None


class RemoveBairros(Mutation):
    class Arguments:
        id = ID(required=True)

    deleted = Boolean()

    def mutate(self, info, id):
        try:
            obj = Bairros.objects.get(pk=id)
            obj.delete()
            return RemoveBairros(deleted=True)
        except Bairros.DoesNotExist:
            return None
