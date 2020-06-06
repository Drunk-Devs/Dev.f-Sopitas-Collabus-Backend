"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_business():
    from seed.models.business import Business
    return Business

def get_category():
    from seed.models.category import Category
    return Category

def get_stat():
    from seed.models.stat import Stat
    return Stat

def get_user():
    from seed.models.user import User
    return User

def get_user_type():
    from seed.models.user_type import UserType
    return UserType

def get_file():
    from seed.models.helpers.file import File
    return File

Business = get_business()
Category = get_category()
Stat = get_stat()
User = get_user()
UserType = get_user_type()
File = get_file()
