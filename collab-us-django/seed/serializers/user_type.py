"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""
from rest_framework import serializers
from dynamic_rest.fields import DynamicRelationField
from seed.helpers.serializer import Serializer
from app.models import UserType

class _UserTypeSerializer(Serializer):  #
    
    user = DynamicRelationField('app.serializers.UserSerializer',source='users',deferred=True, embed=True, many=True, read_only=True)

    user_ids = serializers.PrimaryKeyRelatedField(many=True, source='users', read_only=True)

    class Meta:
        model = UserType
        fields = (
            'id',
            'hash',
            'name',
            'user',
            'user_ids',  
        )