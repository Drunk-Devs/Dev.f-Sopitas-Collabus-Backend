"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.helpers.model import Model

class Stat(Model):  #

    prop_1 = models.IntegerField(default=0)
    prop_2 = models.IntegerField(default=0)
    prop_3 = models.IntegerField(default=0)
    prop_4 = models.IntegerField(default=0)
    comment = models.CharField(max_length=200, blank=True)

    user = models.ForeignKey('models.User', related_name='stats',
        blank=False, null=False, on_delete=models.CASCADE)
    
    @property
    def business(self):
        return self.businesses.all()

    class Meta:
        db_table = '_stat'
        app_label = 'models'
