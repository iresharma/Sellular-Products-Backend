from app.Models.products import Product
import graphene
from pymongo import MongoClient
from app.constants import DB_URL, DB_NAME
from certifi import where
from json import loads


client = MongoClient(DB_URL, tls=True, tlsCAFile=where())
db = client[DB_NAME]
client = db.products


class ProductQueryEnum(graphene.Enum):
    # relevance sorting options
    TOP = 1
    PRICE_LOW_TO_HIGH = 2
    PRICE_HIGH_TO_LOW = 3

    # Query by user
    BY_USER = 4


class Query(graphene.ObjectType):
    product = graphene.Field(Product, id=graphene.String())
    products = graphene.Field(
        graphene.List(Product),
        query=graphene.Enum(ProductQueryEnum),
        page=graphene.Int(default_value=0),
        user=graphene.String(default_value=None)
    )

    def resolve_product(root, info, id):
        return Product(id=id, dbClient=client)

    def resolve_products(self, info, query=None, page: int = 0, user=None) -> list:
        if query == ProductQueryEnum.TOP:
            products = client.aggregate([
                {
                    "$sort": {
                        "viewCount": -1,
                        "bidCount": -1,
                        "viewTime": -1
                    },
                },
                {
                    "$skip": page*20
                },
                {
                    "$limit": 20
                }
            ])
        elif query == ProductQueryEnum.PRICE_LOW_TO_HIGH:
            products = client.aggregate([
                {
                    "$sort": {
                        "askingPrice": 1
                    }
                },
                {
                    "$skip": page*20
                },
                {
                    "$limit": 20
                }
            ])
        elif query == ProductQueryEnum.PRICE_HIGH_TO_LOW:
            products = client.aggregate([
                {
                    "$sort": {
                        "askingPrice": -1
                    }
                },
                {
                    "$skip": page*20
                },
                {
                    "$limit": 20
                }
            ])
        elif query == ProductQueryEnum.BY_USER:
            products = client.aggregate([
                {
                    "$match": {
                        "user": user
                    }
                },
                {
                    "$sort": {
                        "viewCount": -1,
                        "bidCount": -1,
                        "viewTime": -1
                    },
                },
                {
                    "$skip": page*20
                },
                {
                    "$limit": 20
                }
            ])
        return [Product(data=data) for data in products]


schema = graphene.Schema(query=Query, types=[Product])
