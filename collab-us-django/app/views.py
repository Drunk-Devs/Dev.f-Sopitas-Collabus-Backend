"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_business_viewset():
    from seed.views.businesses import _BusinessViewSet
    return _BusinessViewSet

def get_category_viewset():
    from seed.views.categories import _CategoryViewSet
    return _CategoryViewSet

def get_stat_viewset():
    from seed.views.stats import _StatViewSet
    return _StatViewSet

def get_user_viewset():
    from seed.views.users import _UserViewSet
    return _UserViewSet

def get_user_type_viewset():
    from seed.views.user_types import _UserTypeViewSet
    return _UserTypeViewSet

def get_file_view():
    from seed.views.helpers.file import FileView
    return FileView

BusinessViewSet = get_business_viewset()
CategoryViewSet = get_category_viewset()
StatViewSet = get_stat_viewset()
UserViewSet = get_user_viewset()
UserTypeViewSet = get_user_type_viewset()
FileView = get_file_view()
