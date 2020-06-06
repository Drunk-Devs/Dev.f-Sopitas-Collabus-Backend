"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class Business(Model):  #

    name = models.CharField(max_length=150, blank=True)
    address_cords = models.CharField(max_length=512, blank=True)
    contact_1 = models.CharField(max_length=250, blank=True)
    contact_2 = models.CharField(max_length=250, blank=True)
    contact_3 = models.CharField(max_length=250, blank=True)
    contact_4 = models.CharField(max_length=250, blank=True)
    tags = models.TextField(blank=True)
    is_local = models.BooleanField(default=False )
    opening_time = models.DateTimeField(default=datetime.now)
    closing_time = models.DateTimeField(default=datetime.now)
    open_days = models.CharField(max_length=50, blank=True)
    verified = models.BooleanField(default=False )

    user = models.ForeignKey('models.User', related_name='businesses',
        blank=False, null=False, on_delete=models.CASCADE)
    category = models.ForeignKey('models.Category', related_name='businesses',
        blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = '_business'
        app_label = 'models'
