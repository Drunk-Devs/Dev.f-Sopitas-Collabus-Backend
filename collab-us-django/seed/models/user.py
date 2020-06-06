"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from seed.helpers.model import Model

class User(AbstractUser, Model):  #

    user_type = models.ForeignKey('models.UserType', related_name='users',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_user'
        app_label = 'models'
