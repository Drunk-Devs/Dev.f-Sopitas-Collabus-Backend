"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Read only)
  Modify via builder
"""
import graphene

import seed.schema.types
import seed.mutations.business
import seed.mutations.category
import seed.mutations.stat
import seed.mutations.user
import seed.mutations.user_type

class Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    
    saveBusiness = seed.mutations.business.SaveBusinessMutation.Field()
    setBusiness = seed.mutations.business.SetBusinessMutation.Field()
    deleteBusiness = seed.mutations.business.DeleteBusinessMutation.Field()
    saveCategory = seed.mutations.category.SaveCategoryMutation.Field()
    setCategory = seed.mutations.category.SetCategoryMutation.Field()
    deleteCategory = seed.mutations.category.DeleteCategoryMutation.Field()
    saveStat = seed.mutations.stat.SaveStatMutation.Field()
    setStat = seed.mutations.stat.SetStatMutation.Field()
    deleteStat = seed.mutations.stat.DeleteStatMutation.Field()
    saveUser = seed.mutations.user.SaveUserMutation.Field()
    setUser = seed.mutations.user.SetUserMutation.Field()
    deleteUser = seed.mutations.user.DeleteUserMutation.Field()
    saveUserType = seed.mutations.user_type.SaveUserTypeMutation.Field()
    setUserType = seed.mutations.user_type.SetUserTypeMutation.Field()
    deleteUserType = seed.mutations.user_type.DeleteUserTypeMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

