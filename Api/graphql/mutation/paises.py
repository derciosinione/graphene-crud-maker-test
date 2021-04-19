from Api.graphql.query import PaisesType
from Api.models import Paises
from django import forms
from graphene import ID, Boolean, Field, Mutation
from graphene_django.forms.mutation import DjangoModelFormMutation


class PaisesForms(PaisesType):
    class Meta:
        model = Paises
        fields = ("Nome","CodigoPais","DDI","CodPais")


class PaisesMutation(DjangoModelFormMutation):
    class Meta:
        form_class = Paises

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

    # @permission_required('auth.delete_bancos')
    def mutate(self, info, id):
        try:
            obj = Paises.objects.get(pk=id)
            obj.delete()
            return RemovePaises(deleted=True)
        except Paises.DoesNotExist:
            return None