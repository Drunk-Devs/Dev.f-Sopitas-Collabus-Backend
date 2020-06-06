"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_business_serializer():
    from seed.serializers.business import _BusinessSerializer
    return _BusinessSerializer

def get_category_serializer():
    from seed.serializers.category import _CategorySerializer
    return _CategorySerializer

def get_stat_serializer():
    from seed.serializers.stat import _StatSerializer
    return _StatSerializer

def get_user_serializer():
    from seed.serializers.user import _UserSerializer
    return _UserSerializer

def get_user_type_serializer():
    from seed.serializers.user_type import _UserTypeSerializer
    return _UserTypeSerializer

def get_file_serializer():
    from seed.serializers.helpers.file import FileSerializer
    return FileSerializer

BusinessSerializer = get_business_serializer()
CategorySerializer = get_category_serializer()
StatSerializer = get_stat_serializer()
UserSerializer = get_user_serializer()
UserTypeSerializer = get_user_type_serializer()
FileSerializer = get_file_serializer()
