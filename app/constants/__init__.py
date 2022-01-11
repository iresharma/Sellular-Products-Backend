from os import environ

DB_URL = environ.get('SELLULAR_DBURL')
DB_NAME = 'Sellular_app'

# AWS S3
AWS_ACCESS_KEY = environ.get('SELLULAR_AWS_S3_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = environ.get('SELLULAR_AWS_S3_SECRET_KEY')

PRODUCT_BUCKET_NAME = 'sellular-product-images'