"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""
from seed.helpers.serializer import Serializer
from app.models import User

class _UserSerializer(Serializer):  #

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
        )
