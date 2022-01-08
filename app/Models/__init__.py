# Importing types
from app.Models.types.products import Product
from app.Models.types.category import Category

# Import Query
from app.Models.Query import Query

# Importing Mutation
from app.Models.mutations import Mutations

import graphene


schema = graphene.Schema(query=Query, mutation=Mutations, types=[Product, Category])