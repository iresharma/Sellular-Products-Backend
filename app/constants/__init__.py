from os import environ

DB_URL = environ.get('SELLULAR_DBURL')
DB_NAME = 'Sellular_app'

# AWS S3
AWS_ACCESS_KEY = environ.get('SELLULAR_AWS_S3_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = environ.get('SELLULAR_AWS_S3_SECRET_KEY')

PRODUCT_BUCKET_NAME = 'sellular-product-images'

# Auth 0
ALGORITHMS = ["RS256"]
AUTH0_DOMAIN = environ.get('SELLULAR_AUTH0_DOMAIN')
API_AUDIENCE = environ.get('SELLULAR_AUTH0_AUDIENCE')