from flask_graphql import GraphQLView
from app.heplers.auth import check_auth

class ProtectedGraphQlView(GraphQLView):
    def dispatch_request(self, *args, **kwargs):
        check_auth()
        return super().dispatch_request(*args, **kwargs)