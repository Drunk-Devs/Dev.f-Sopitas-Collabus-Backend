"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import User
from app.models import UserType
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _UserSerializer(Serializer):  #
    
    user_type = DynamicRelationField('app.serializers.UserTypeSerializer', 
        deferred=True, embed=True, read_only=True)

    user_type_id = serializers.PrimaryKeyRelatedField(source='user_type', queryset=UserType.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = User
        fields = (
            'id',
            'hash',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'user_type',
            'user_type_id',  
        )
