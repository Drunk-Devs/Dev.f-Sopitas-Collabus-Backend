"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import UserType
from app.models import File
from seed.schema.types import UserType as UserTypeType

class SaveUserTypeMutation(graphene.Mutation):
    
    userType = graphene.Field(UserTypeType)
    
    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, **kwargs):

        user_type = {}
        if "name" in kwargs: user_type["name"] = kwargs["name"]
        user_type = UserType.objects.create(**user_type)
        user_type.save()
    
        return SaveUserTypeMutation(userType=user_type)

class SetUserTypeMutation(graphene.Mutation):
    
    userType = graphene.Field(UserTypeType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        user_type = UserType.objects.get(pk=kwargs["id"])
        if "name" in kwargs: user_type.name = kwargs["name"]
        user_type.save()
    
        return SetUserTypeMutation(userType=user_type)

class DeleteUserTypeMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        user_type = UserType.objects.get(pk=kwargs["id"])
        user_type.delete()
        return DeleteUserTypeMutation(id=id)
