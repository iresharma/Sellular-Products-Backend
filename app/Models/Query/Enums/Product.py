import graphene

class ProductQueryEnum(graphene.Enum):
    # relevance sorting options
    TOP = 1
    PRICE_LOW_TO_HIGH = 2
    PRICE_HIGH_TO_LOW = 3

    # Query by user
    BY_USER = 4