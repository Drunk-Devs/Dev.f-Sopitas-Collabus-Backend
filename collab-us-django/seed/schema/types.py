"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django.types import DjangoObjectType
from seed.schema.util.query_util import parse_query
from app.models import Business as BusinessModel
from app.models import Category as CategoryModel
from app.models import Stat as StatModel
from app.models import User as UserModel
from app.models import UserType as UserTypeModel
from app.models import File as FileModel

class Business(DjangoObjectType):
    class Meta:
        model = BusinessModel

class Category(DjangoObjectType):
    class Meta:
        model = CategoryModel

class Stat(DjangoObjectType):
    class Meta:
        model = StatModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel
        exclude = ('password',)

class UserType(DjangoObjectType):
    class Meta:
        model = UserTypeModel

class File(DjangoObjectType):
    class Meta:
        model = FileModel
        description = 'Represents a File object'

class Query(object):
    
    businesses = graphene.List(Business, query=graphene.String())
    business = graphene.Field(Business, id=graphene.Int())
    categories = graphene.List(Category, query=graphene.String())
    category = graphene.Field(Category, id=graphene.Int())
    stats = graphene.List(Stat, query=graphene.String())
    stat = graphene.Field(Stat, id=graphene.Int())
    users = graphene.List(User, query=graphene.String())
    user = graphene.Field(User, id=graphene.Int())
    userTypes = graphene.List(UserType, query=graphene.String())
    userType = graphene.Field(UserType, id=graphene.Int())
    files = graphene.List(File, query=graphene.String())
    file = graphene.Field(File, id=graphene.Int())

    def resolve_businesses(self, info, **kwargs):
        if "query" in kwargs:
            return parse_query(kwargs["query"], BusinessModel)
        return BusinessModel.objects.all()
    def resolve_business(self, info, id):
        return BusinessModel.objects.get(pk=id)
    
    def resolve_categories(self, info, **kwargs):
        if "query" in kwargs:
            return parse_query(kwargs["query"], CategoryModel)
        return CategoryModel.objects.all()
    def resolve_category(self, info, id):
        return CategoryModel.objects.get(pk=id)
    
    def resolve_stats(self, info, **kwargs):
        if "query" in kwargs:
            return parse_query(kwargs["query"], StatModel)
        return StatModel.objects.all()
    def resolve_stat(self, info, id):
        return StatModel.objects.get(pk=id)
    
    def resolve_users(self, info, **kwargs):
        if "query" in kwargs:
            return parse_query(kwargs["query"], UserModel)
        return UserModel.objects.all()
    def resolve_user(self, info, id):
        return UserModel.objects.get(pk=id)
    
    def resolve_userTypes(self, info, **kwargs):
        if "query" in kwargs:
            return parse_query(kwargs["query"], UserTypeModel)
        return UserTypeModel.objects.all()
    def resolve_userType(self, info, id):
        return UserTypeModel.objects.get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        if "query" in kwargs:
            return parse_query(kwargs["query"], FileModel)
        return FileModel.objects.all()
    def resolve_file(self, info, id):
        return FileModel.objects.get(pk=id)