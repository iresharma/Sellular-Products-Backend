# Products import
from app.Models.types.products import Product
from app.Models.Query.query_functions import product_ranks
from app.Models.Query.Enums.Product import ProductQueryEnum

# Category imports
from app.Models.types.category import Category

import graphene
from pymongo import MongoClient
from app.constants import DB_URL, DB_NAME
from certifi import where


client = MongoClient(DB_URL, tls=True, tlsCAFile=where())
db = client[DB_NAME]


class Query(graphene.ObjectType):
    product = graphene.Field(Product, id=graphene.String(), required=True)
    products = graphene.Field(
        graphene.List(Product),
        query=graphene.Argument(ProductQueryEnum, required=True),
        page=graphene.Int(default_value=0),
        user=graphene.String(default_value=None)
    )

    products_count = graphene.Field(graphene.Int, default_value=0)

    search = graphene.Field(Product, search=graphene.String(default_value=""))

    category = graphene.Field(Category, id=graphene.String())

    categories = graphene.Field(graphene.List(Category))

    def resolve_products_count(root, info):
        count = db.products.count_documents({})
        return count

    def resolve_product(root, info, id):
        return Product(id=id, dbClient=db)

    def resolve_products(self, info, query=None, page: int = 0, user=None) -> list:
        products = product_ranks(db , query, page, user)
        return [Product(data=data, dbClient=db) for data in products]

    def resolve_search(root, info, search=None):
        products = db.products.find({
            "$text": {
                "$title": search
            },
            "$text": {
                "$description": search
            }
        }, {"score": {"$meta": "textScore"}})
        return [Product(data=data, dbClient=db) for data in products]

    def resolve_category(root, info, id=None):
        return Category(id=id, dbClient=db)

    def resolve_categories(root, info):
        categories = db.categories.find()
        return [Category(data=data, dbClient=db) for data in categories]

