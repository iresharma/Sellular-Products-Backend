import graphene


class Product(graphene.ObjectType):
    '''
        This is the class for the Product object
    '''

    # MongoDb id
    id = graphene.String()

    title = graphene.String(value=graphene.String(default_value=""))
    description = graphene.String(value=graphene.String(default_value=""))
    askingPrice = graphene.Float(value=graphene.Float(default_value=0.0))
    images = graphene.List(graphene.String)
    category = graphene.String()

    # Analytics pointers
    viewCount = graphene.Int()
    bidCount = graphene.Int()
    viewTime = graphene.Float()  # in seconds

    # DB client
    dbClient = None

    # access variable
    product = {}

    def __init__(self, id=None, data=None, dbClient=None):
        if dbClient:
            self.dbClient = dbClient
        if id:
            self.get_product_by_id(id)
        if data:
            self.product = data
            self.dbClient.products.update_one(
                {"_id": id}, {"$inc": {"viewCount": 1}})
            # self.dbClient.categories.update_one(
            #     {"_id": data['category']}, {"$inc": {"nHits": 1}})

    def resolve_id(root, info, value=None):
        return root.product['_id']

    def resolve_title(root, info, value=None):
        return root.product['title']

    def resolve_description(root, info, value=None):
        return root.product['description']

    def resolve_askingPrice(root, info, value=None):
        return root.product['askingPrice']

    def resolve_images(root, info, value=None):
        return root.product['images']

    def resolve_category(root, info, value=None):
        return root.product['category']

    def resolve_viewCount(root, info, value=None):
        return root.product['viewCount']

    def resolve_bidCount(root, info, value=None):
        return root.product['bidCount']

    def resolve_viewTime(root, info, value=None):
        return root.product['viewTime']

    # Database functions

    def get_product_by_id(self, id):
        '''
            Db function to get a product by id
        '''
        data = self.dbClient.products.find_one({"_id": id})
        self.dbClient.products.update_one(
            {"_id": id}, {"$inc": {"viewCount": 1}})
        self.dbClient.categories.update_one(
            {"_id": data['category']}, {"$inc": {"nHits": 1}})
        self.product = data
