from app import app
import boto
from app.heplers.auth import requires_auth
from app.constants import AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, PRODUCT_BUCKET_NAME

@requires_auth
@app.route('/s3', methods=['GET', 'POST', 'DELETE', 'PUT'])
def s3Handler():
    try:
        conn = boto.connect_s3(AWS_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, is_secure=False)
    except Exception as e:
        return "Error in connecting to S3: " + str(e)
    
    print(PRODUCT_BUCKET_NAME)
    bucket = conn.get_bucket(PRODUCT_BUCKET_NAME)
    # try:
    # except Exception as e:
    #     return "Error in getting bucket: " + str(e)
    return "Hello S3"