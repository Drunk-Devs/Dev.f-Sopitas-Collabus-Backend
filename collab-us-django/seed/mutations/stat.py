"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Stat
from app.models import Business
from app.models import User
from app.models import File
from seed.schema.types import Stat as StatType

class SaveStatMutation(graphene.Mutation):
    
    stat = graphene.Field(StatType)
    
    class Arguments:
        prop1 = graphene.Int(required=True)
        prop2 = graphene.Int(required=True)
        prop3 = graphene.Int(required=True)
        prop4 = graphene.Int(required=True)
        comment = graphene.String(required=True)
        user = graphene.Int(required=True)

    def mutate(self, info, **kwargs):

        stat = {}
        if "prop1" in kwargs: stat["prop_1"] = kwargs["prop1"]
        if "prop2" in kwargs: stat["prop_2"] = kwargs["prop2"]
        if "prop3" in kwargs: stat["prop_3"] = kwargs["prop3"]
        if "prop4" in kwargs: stat["prop_4"] = kwargs["prop4"]
        if "comment" in kwargs: stat["comment"] = kwargs["comment"]
        if "user" in kwargs:
             user = User.objects.get(pk = kwargs["user"])
             stat["user"] = user
        stat = Stat.objects.create(**stat)
        stat.save()
    
        return SaveStatMutation(stat=stat)

class SetStatMutation(graphene.Mutation):
    
    stat = graphene.Field(StatType)
    
    class Arguments:
        id = graphene.Int(required=True)
        prop1 = graphene.Int(required=False)
        prop2 = graphene.Int(required=False)
        prop3 = graphene.Int(required=False)
        prop4 = graphene.Int(required=False)
        comment = graphene.String(required=False)
        user = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        stat = Stat.objects.get(pk=kwargs["id"])
        if "prop1" in kwargs: stat.prop_1 = kwargs["prop1"]
        if "prop2" in kwargs: stat.prop_2 = kwargs["prop2"]
        if "prop3" in kwargs: stat.prop_3 = kwargs["prop3"]
        if "prop4" in kwargs: stat.prop_4 = kwargs["prop4"]
        if "comment" in kwargs: stat.comment = kwargs["comment"]
        if "user" in kwargs:
             user = User.objects.get(pk = kwargs["user"])
             stat.user = user
        stat.save()
    
        return SetStatMutation(stat=stat)

class DeleteStatMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        stat = Stat.objects.get(pk=kwargs["id"])
        stat.delete()
        return DeleteStatMutation(id=id)
