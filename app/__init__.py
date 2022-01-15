from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from app.Models import schema
from app.heplers.protectedGraphQlView import ProtectedGraphQlView

from flask import request

app = Flask(__name__)
CORS(app)

from app.Routes import s3

app.add_url_rule(
    '/graphql',
    view_func=ProtectedGraphQlView.as_view('graphql', schema=schema, graphiql=True)
)