"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Category
from app.models import File
from seed.schema.types import Category as CategoryType

class SaveCategoryMutation(graphene.Mutation):
    
    category = graphene.Field(CategoryType)
    
    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, **kwargs):

        category = {}
        if "name" in kwargs: category["name"] = kwargs["name"]
        category = Category.objects.create(**category)
        category.save()
    
        return SaveCategoryMutation(category=category)

class SetCategoryMutation(graphene.Mutation):
    
    category = graphene.Field(CategoryType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        category = Category.objects.get(pk=kwargs["id"])
        if "name" in kwargs: category.name = kwargs["name"]
        category.save()
    
        return SetCategoryMutation(category=category)

class DeleteCategoryMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        category = Category.objects.get(pk=kwargs["id"])
        category.delete()
        return DeleteCategoryMutation(id=id)
