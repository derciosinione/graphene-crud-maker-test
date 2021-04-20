from graphene import ObjectType 
from Core.utils import CustomNode 
from graphene_django.filter import DjangoFilterConnectionField 

from .User import UserType 
from .Bairros import BairrosType 
from .Paises import PaisesType 
from .Provincias import ProvinciasType 
from .Cidades import CidadesType 
from .Generos import GenerosType 
from .Municipios import MunicipiosType 
from .Ruas import RuasType 
from .User_permissions import User_permissionsType 


class Query(ObjectType):
	user = CustomNode.Field(UserType) 
	all_user = DjangoFilterConnectionField(UserType) 

	bairros = CustomNode.Field(BairrosType) 
	all_bairros = DjangoFilterConnectionField(BairrosType) 

	paises = CustomNode.Field(PaisesType) 
	all_paises = DjangoFilterConnectionField(PaisesType) 

	provincias = CustomNode.Field(ProvinciasType) 
	all_provincias = DjangoFilterConnectionField(ProvinciasType) 

	cidades = CustomNode.Field(CidadesType) 
	all_cidades = DjangoFilterConnectionField(CidadesType) 

	generos = CustomNode.Field(GenerosType) 
	all_generos = DjangoFilterConnectionField(GenerosType) 

	municipios = CustomNode.Field(MunicipiosType) 
	all_municipios = DjangoFilterConnectionField(MunicipiosType) 

	ruas = CustomNode.Field(RuasType) 
	all_ruas = DjangoFilterConnectionField(RuasType) 

	user_permissions = CustomNode.Field(User_permissionsType) 
	all_user_permissions = DjangoFilterConnectionField(User_permissionsType) 


