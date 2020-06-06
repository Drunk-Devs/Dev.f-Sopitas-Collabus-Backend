"""
__Seed builder__v0.1.8

  Base routes:
    - /businesses
    - /categories
    - /stats
    - /users
    - /user_types
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
