"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Stat
from app.serializers import StatSerializer

class _StatViewSet(ViewSet):  #

    serializer_class = StatSerializer
    queryset = Stat.objects.all()
