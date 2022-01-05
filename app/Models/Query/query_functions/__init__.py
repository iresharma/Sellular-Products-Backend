from app.Models.Query.Enums.Product import ProductQueryEnum

def product_ranks(db , query, page, user) -> list:
    if query == ProductQueryEnum.TOP:
        products = db.products.aggregate([
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
        products = db.products.aggregate([
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
        products = db.products.aggregate([
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
        products = db.products.aggregate([
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

    return products