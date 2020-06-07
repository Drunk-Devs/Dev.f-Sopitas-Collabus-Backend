"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""
from seed.helpers.serializer import Serializer
from app.models import Category

class _CategorySerializer(Serializer):  #

    class Meta:
        model = Category
        fields = (
            'id',
            'hash',
            'name',  
        )
