from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from app.Models import schema

app = Flask(__name__)
CORS(app)


@app.route('/s3', methods=['GET', 'POST', 'DELETE', 'PUT'])
def s3Handler():
    return "Hello S3"


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)
