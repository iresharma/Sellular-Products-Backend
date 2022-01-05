from app.Models.products import Product
from app.Models.query import Query
import graphene


schema = graphene.Schema(query=Query, types=[Product])
