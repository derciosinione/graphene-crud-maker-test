from django.db import models
from uuid import uuid4
from .User import User

class User_permissions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_permis')
    permission = models.ForeignKey('auth.Permission', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.permission.name}'

        class Meta:
            verbose_name_plural = "Permissões de Usuários"
