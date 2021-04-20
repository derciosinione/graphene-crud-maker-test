from graphene import ObjectType

from .User import UserMutation, RemoveUser 
from .Bairros import BairrosMutation, RemoveBairros 
from .Paises import PaisesMutation, RemovePaises 
from .Provincias import ProvinciasMutation, RemoveProvincias 
from .Cidades import CidadesMutation, RemoveCidades 
from .Generos import GenerosMutation, RemoveGeneros 
from .Municipios import MunicipiosMutation, RemoveMunicipios 
from .Ruas import RuasMutation, RemoveRuas 
from .User_permissions import User_permissionsMutation, RemoveUser_permissions 


class Mutation(ObjectType):
	user = UserMutation.Field() 
	remove_user = RemoveUser.Field() 

	bairros = BairrosMutation.Field() 
	remove_bairros = RemoveBairros.Field() 

	paises = PaisesMutation.Field() 
	remove_paises = RemovePaises.Field() 

	provincias = ProvinciasMutation.Field() 
	remove_provincias = RemoveProvincias.Field() 

	cidades = CidadesMutation.Field() 
	remove_cidades = RemoveCidades.Field() 

	generos = GenerosMutation.Field() 
	remove_generos = RemoveGeneros.Field() 

	municipios = MunicipiosMutation.Field() 
	remove_municipios = RemoveMunicipios.Field() 

	ruas = RuasMutation.Field() 
	remove_ruas = RemoveRuas.Field() 

	user_permissions = User_permissionsMutation.Field() 
	remove_user_permissions = RemoveUser_permissions.Field() 

