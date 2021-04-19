from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False)
    user_permissions = models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                              related_name='user_set', to='auth.Permission', through='User_permissions')

    def save(self, *args, **kwargs):
        if self.id == None:
            self.id = uuid4()
        super().save(*args, **kwargs)