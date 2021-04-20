from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True)))),
    path("", csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True)))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
