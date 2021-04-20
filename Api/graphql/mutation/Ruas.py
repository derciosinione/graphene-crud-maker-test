from graphene import Field
from django import forms
from graphene import ID, Mutation, Boolean
from graphene_django.forms.mutation import DjangoModelFormMutation

from Api.models import Ruas
from Api.graphql.query import RuasType


class RuasForm(forms.ModelForm):
    class Meta:
        model = Ruas
        fields = ['bairroid', 'codrua', 'nome']


class RuasMutation(DjangoModelFormMutation):
    class Meta:
        form_class = RuasForm

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

    def mutate(self, info, id):
        try:
            obj = Ruas.objects.get(pk=id)
            obj.delete()
            return RemoveRuas(deleted=True)
        except Ruas.DoesNotExist:
            return None
