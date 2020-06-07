"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Business
from app.models import User
from app.models import Category
from seed.schema.types import Business as BusinessType

class SaveBusinessMutation(graphene.Mutation):
    
    business = graphene.Field(BusinessType)
    
    class Arguments:
        name = graphene.String(required=True)
        addressCords = graphene.String(required=True)
        contact1 = graphene.String(required=True)
        contact2 = graphene.String(required=True)
        contact3 = graphene.String(required=True)
        contact4 = graphene.String(required=True)
        tags = graphene.String(required=True)
        isLocal = graphene.Boolean(required=True)
        openingTime = graphene.DateTime(required=True)
        closingTime = graphene.DateTime(required=True)
        openDays = graphene.String(required=True)
        verified = graphene.Boolean(required=True)
        user = graphene.Int(required=True)
        category = graphene.Int(required=True)

    def mutate(self, info, **kwargs):

        business = {}
        if "name" in kwargs: business["name"] = kwargs["name"]
        if "addressCords" in kwargs: business["address_cords"] = kwargs["addressCords"]
        if "contact1" in kwargs: business["contact_1"] = kwargs["contact1"]
        if "contact2" in kwargs: business["contact_2"] = kwargs["contact2"]
        if "contact3" in kwargs: business["contact_3"] = kwargs["contact3"]
        if "contact4" in kwargs: business["contact_4"] = kwargs["contact4"]
        if "tags" in kwargs: business["tags"] = kwargs["tags"]
        if "isLocal" in kwargs: business["is_local"] = kwargs["isLocal"]
        if "openingTime" in kwargs: business["opening_time"] = kwargs["openingTime"]
        if "closingTime" in kwargs: business["closing_time"] = kwargs["closingTime"]
        if "openDays" in kwargs: business["open_days"] = kwargs["openDays"]
        if "verified" in kwargs: business["verified"] = kwargs["verified"]
        if "user" in kwargs:
             user = User.objects.get(pk = kwargs["user"])
             business["user"] = user
        if "category" in kwargs:
             category = Category.objects.get(pk = kwargs["category"])
             business["category"] = category
        business = Business.objects.create(**business)
        business.save()
    
        return SaveBusinessMutation(business=business)

class SetBusinessMutation(graphene.Mutation):
    
    business = graphene.Field(BusinessType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        addressCords = graphene.String(required=False)
        contact1 = graphene.String(required=False)
        contact2 = graphene.String(required=False)
        contact3 = graphene.String(required=False)
        contact4 = graphene.String(required=False)
        tags = graphene.String(required=False)
        isLocal = graphene.Boolean(required=False)
        openingTime = graphene.DateTime(required=False)
        closingTime = graphene.DateTime(required=False)
        openDays = graphene.String(required=False)
        verified = graphene.Boolean(required=False)
        user = graphene.Int(required=False)
        category = graphene.Int(required=False)

    def mutate(self, info, **kwargs):

        business = Business.objects.get(pk=kwargs["id"])
        if "name" in kwargs: business.name = kwargs["name"]
        if "addressCords" in kwargs: business.address_cords = kwargs["addressCords"]
        if "contact1" in kwargs: business.contact_1 = kwargs["contact1"]
        if "contact2" in kwargs: business.contact_2 = kwargs["contact2"]
        if "contact3" in kwargs: business.contact_3 = kwargs["contact3"]
        if "contact4" in kwargs: business.contact_4 = kwargs["contact4"]
        if "tags" in kwargs: business.tags = kwargs["tags"]
        if "isLocal" in kwargs: business.is_local = kwargs["isLocal"]
        if "openingTime" in kwargs: business.opening_time = kwargs["openingTime"]
        if "closingTime" in kwargs: business.closing_time = kwargs["closingTime"]
        if "openDays" in kwargs: business.open_days = kwargs["openDays"]
        if "verified" in kwargs: business.verified = kwargs["verified"]
        if "user" in kwargs:
             user = User.objects.get(pk = kwargs["user"])
             business.user = user
        if "category" in kwargs:
             category = Category.objects.get(pk = kwargs["category"])
             business.category = category
        business.save()
    
        return SetBusinessMutation(business=business)

class DeleteBusinessMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        business = Business.objects.get(pk=kwargs["id"])
        business.delete()
        return DeleteBusinessMutation(id=id)
