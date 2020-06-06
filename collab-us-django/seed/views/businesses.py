"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Business
from app.serializers import BusinessSerializer

class _BusinessViewSet(ViewSet):  #

    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
