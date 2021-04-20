from django.contrib import admin
from .models import ( User_permissions, Generos,)


admin.site.register(Generos)
admin.site.register(User_permissions)
