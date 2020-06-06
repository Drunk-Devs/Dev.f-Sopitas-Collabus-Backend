"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from seed.helpers.model_admin import ModelAdminClass
from app.models import Business
from app.models import Category
from app.models import Stat
from app.models import User
from app.models import UserType
from app.models import File

class _Admin:  #

  @staticmethod
  def register():  #
      
      class BusinessAdmin(ModelAdminClass(Business)):
          pass
      
      class CategoryAdmin(ModelAdminClass(Category)):
          pass
      
      class StatAdmin(ModelAdminClass(Stat)):
          pass
      
      class UserAdmin(ModelAdminClass(User)):
          pass
      
      class UserTypeAdmin(ModelAdminClass(UserType)):
          pass
      
      class FileAdmin(ModelAdminClass(File)):
          pass
      admin.site.register(Business, BusinessAdmin)
      admin.site.register(Category, CategoryAdmin)
      admin.site.register(Stat, StatAdmin)
      admin.site.register(User, UserAdmin)
      admin.site.register(UserType, UserTypeAdmin)
      admin.site.register(File, FileAdmin)
