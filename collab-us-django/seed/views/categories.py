"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Category
from app.serializers import CategorySerializer

class _CategoryViewSet(ViewSet):  #

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
