"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""
from rest_framework import serializers
from dynamic_rest.fields import DynamicRelationField
from seed.helpers.serializer import Serializer
from app.models import Stat
from app.models import User

class _StatSerializer(Serializer):  #
    
    business = DynamicRelationField('app.serializers.BusinessSerializer',source='businesses',deferred=True, embed=True, many=True, read_only=True)
    user = DynamicRelationField('app.serializers.UserSerializer', 
        deferred=True, embed=True, read_only=True)

    business_ids = serializers.PrimaryKeyRelatedField(many=True, source='businesses', read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = Stat
        fields = (
            'id',
            'hash',
            'prop_1',
            'prop_2',
            'prop_3',
            'prop_4',
            'comment',
            'business',
            'user',
            'business_ids',
            'user_id',  
        )
