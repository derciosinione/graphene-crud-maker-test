from Api.graphql.query import ProvinciasType
from Api.models import Provincias
from django import forms
from graphene import ID, Boolean, Field, Mutation
from graphene_django.forms.mutation import DjangoModelFormMutation


class ProvinciasForms(ProvinciasType):
    class Meta:
        model = Provincias
        fields = ("Nome", "CodProvincia")


class ProvinciasMutation(DjangoModelFormMutation):
    class Meta:
        form_class = Provincias

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

    # @permission_required('auth.delete_bancos')
    def mutate(self, info, id):
        try:
            obj = Provincias.objects.get(pk=id)
            obj.delete()
            return RemoveProvincias(deleted=True)
        except Provincias.DoesNotExist:
            return None