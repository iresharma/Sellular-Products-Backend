from app.Models.mutations.products.createProduct import CreateProduct
import graphene


class Mutations(graphene.ObjectType):
    create_product = CreateProduct.Field()