"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.urls import path, include
from django.conf.urls import url
from dynamic_rest.routers import DynamicRouter

from app.views import BusinessViewSet
from app.views import CategoryViewSet
from app.views import StatViewSet
from app.views import UserViewSet
from app.views import UserTypeViewSet
from app.views import FileView

router = DynamicRouter()
router.register(r'businesses', BusinessViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'stats', StatViewSet)
router.register(r'users', UserViewSet)
router.register(r'user_types', UserTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    url(r'^auth/', include('rest_auth.urls'))
]