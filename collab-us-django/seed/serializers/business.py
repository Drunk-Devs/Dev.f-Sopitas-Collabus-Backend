"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import Business
from app.models import User
from app.models import Category
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _BusinessSerializer(Serializer):  #
    
    user = DynamicRelationField('app.serializers.UserSerializer', 
        deferred=True, embed=True, read_only=True)
    category = DynamicRelationField('app.serializers.CategorySerializer', 
        deferred=True, embed=True, read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all(), 
        required=True, allow_null=False)
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = Business
        fields = (
            'id',
            'hash',
            'name',
            'address_cords',
            'contact_1',
            'contact_2',
            'contact_3',
            'contact_4',
            'tags',
            'is_local',
            'opening_time',
            'closing_time',
            'open_days',
            'verified',
            'user',
            'category',
            'user_id',
            'category_id',  
        )
