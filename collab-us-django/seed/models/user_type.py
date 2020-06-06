"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class UserType(Model):  #
    
    NAMES = (
        ('OWNER', 'OWNER'),
        ('CLIENT', 'CLIENT'),
    )

    name = models.CharField(max_length=64, choices=NAMES,
        blank=False)

    class Meta:
        db_table = '_user_type'
        app_label = 'models'