import graphql_jwt
from graphene import Schema, Field
from django.dispatch import receiver
from graphql_jwt.refresh_token.signals import refresh_token_rotated
from graphql_jwt.relay import JSONWebTokenMutation

# Execute Crud Maker
from .crud_maker.core import CrudMaker
CrudMaker(app_name = 'Api')

# Here is where you will put your schema from app you have created
from Api.graphql.query import UserType
from Api.graphql.schema import Query as ApiQuery, Mutation as ApiMutation


class ObtainJSONWebToken(JSONWebTokenMutation):
    user = Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class Query(ApiQuery):
    pass


class Mutation(ApiMutation):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.refresh_token.relay.DeleteRefreshTokenCookie.Field()

    # One time only use refresh token
    @receiver(refresh_token_rotated)
    def revoke_refresh_token(sender, request, refresh_token, **kwargs):
        refresh_token.revoke(request)


schema = Schema(query=Query, mutation=Mutation)

    