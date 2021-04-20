# field_name = [field.name for field in Generos._meta.get_fields()]
# field_name.remove('id')


from graphene_django import DjangoObjectType
from Core.utils import CustomNode
from Api.models import Generos
    

class GenerosType(DjangoObjectType):
    class Meta:
        model = Generos
        filter_fields = {
            'id': ['exact',],
        }   
        interfaces = (CustomNode,)


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        field = [field.name for field in User._meta.get_fields()]
        exclude_fields = ['id', 'data_atualizacao', 'user_permis', 'refresh_tokens', 'logentry']
        
        # Removing exclude_fields
        for item in exclude_fields:
            if field.__contains__(item):
                field.remove(item)        
        
        fields = field