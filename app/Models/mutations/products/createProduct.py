import graphene

class CreateProduct(graphene.Mutation):
    class Arguments:
        title = graphene.String(value = graphene.String(default_value = ""))
        description = graphene.String(value = graphene.String(default_value = ""))
        askingPrice = graphene.Float(value = graphene.Float(default_value = 0.0))
        images = graphene.List(graphene.String)
        category = graphene.String()