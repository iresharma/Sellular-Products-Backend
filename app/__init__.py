from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from app.Models import schema

app = Flask(__name__)
CORS(app)

# from app.routes import routes

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)