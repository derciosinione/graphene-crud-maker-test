from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import Generos
from Api.graphql.query import GenerosType
from django.apps import apps


class GenerosForm(forms.ModelForm):
    class Meta:
        model = Generos
        field = [field.name for field in Generos._meta.get_fields()]
        exclude_fields = ['id', 'datacriacao','dataatualizacao', 'data_criacao', 'data_atualizacao']

        # Removing exclude_fields
        for item in exclude_fields:
            if field.__contains__(item):
                field.remove(item)
                
        fields = field


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

    def mutate(self, info, id):
        try:
            obj = Generos.objects.get(pk=id)
            obj.delete()
            return RemoveGenero(deleted=True)
        except Generos.DoesNotExist:
            return None