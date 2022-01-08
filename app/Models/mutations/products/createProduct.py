import graphene

from app.Models.types.products import Product
from uuid import uuid4


from pymongo import MongoClient
from app.constants import DB_URL, DB_NAME
from certifi import where


client = MongoClient(DB_URL, tls=True, tlsCAFile=where())
db = client[DB_NAME]


class CreateProduct(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        askingPrice = graphene.Float()
        images = graphene.List(graphene.String)
        category = graphene.String()

    ok = graphene.Boolean()
    product = graphene.Field(lambda: Product)

    def mutate(root, info, title, description, askingPrice, images, category):
        db.products.insert_one({
            "_id": uuid4().hex,
            "title": title,
            "description": description,
            "askingPrice": askingPrice,
            "images": images,
            "category": category,
            "viewCount": 0,
            "viewTime": 0,
            "bidCount": 0
        })
        return CreateProduct(
            ok=True,
            product=Product(id=db.products.find_one(
                {"title": title})["_id"], dbClient=db)
        )
