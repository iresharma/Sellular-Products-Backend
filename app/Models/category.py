import graphene
from app.Models.products import Product

class Category(graphene.ObjectType):
    '''
        This is a class for the category object
    '''

    # MongoDb id
    id = graphene.String()

    title = graphene.String()
    description = graphene.String()
    products = graphene.List(Product, default_value = [])
    icons = graphene.String()

    # Analytics pointers
    nProducts = graphene.Int()
    nHits = graphene.Int()

    # DB client
    dbClient = None

    # access variable
    category = {}

    def __init__(self, id=None, data=None, dbClient=None):
        if dbClient:
            self.dbClient = dbClient
        if id:
            self.get_category_by_id(id)
        elif data:
            self.category = data

    def resolve_id(root, info, value=None):
        return root.category['_id']

    def resolve_title(root, info, value=None):
        return root.category['title']

    def resolve_description(root, info, value=None):
        return root.category['description']

    def resolve_products(root, info, value=None):
        return root.category['products']

    def resolve_icons(root, info, value=None):
        return root.category['icons']

    def resolve_nProducts(root, info, value=None):
        return len(root.category['products'])

    def resolve_nHits(root, info, value=None):
        return root.category['nHits']

    def get_category_by_id(self, id):
        data = self.dbClient.categories.find_one({'_id': id})
        self.dbClient.categories.update_one({'_id': id}, {'$inc': {'nHits': 1}})
        self.category = data