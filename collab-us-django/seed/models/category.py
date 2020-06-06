"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class Category(Model):  #
    
    NAMES = (
        ('SALUD', 'salud'),
        ('ENTRETENIMIENTO', 'entretenimiento'),
        ('ABARROTES', 'abarrotes'),
        ('CUIDADO PERSONAL', 'cuidado personal'),
        ('BELLEZA', 'belleza'),
        ('ACTIVIDAD FISICA', 'actividad fisica'),
        ('CONSTRUCCION Y MANTENIMIENTO', 'construccion y mantenimiento'),
        ('TRANSPORTE', 'transporte'),
        ('RESTAURANTES', 'restaurantes'),
        ('COMIDA', 'comida'),
        ('CONTRATISTAS', 'contratistas'),
    )

    name = models.CharField(max_length=64, choices=NAMES,
        blank=False)

    class Meta:
        db_table = '_category'
        app_label = 'models'
