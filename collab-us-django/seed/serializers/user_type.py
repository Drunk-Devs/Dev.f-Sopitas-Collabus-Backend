"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import UserType
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _UserTypeSerializer(Serializer):  #

    class Meta:
        model = UserType
        fields = (
            'id',
            'hash',
            'name',  
        )