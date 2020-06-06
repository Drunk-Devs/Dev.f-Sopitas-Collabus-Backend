"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import UserType
from app.serializers import UserTypeSerializer

class _UserTypeViewSet(ViewSet):  #

    serializer_class = UserTypeSerializer
    queryset = UserType.objects.all()
