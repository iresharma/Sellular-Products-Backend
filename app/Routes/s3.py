from app import app
import boto
from app.heplers.auth import requires_auth
from app.constants import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, PRODUCT_BUCKET_NAME

# @requires_auth


@app.route('/s3', methods=['GET', 'POST', 'DELETE', 'PUT'])
def s3Handler():
    # function to connect to s3 bucket
    try:
        s3 = boto.connect_s3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY)
    except Exception as e:
        print(e)
        return 'Internal Server error', 503
    try:
        bucket = s3.get_bucket(PRODUCT_BUCKET_NAME)
    except Exception as e:
        print(e)
        return 'Internal Server error', 503
    return 'connected', 200
