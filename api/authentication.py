from rest_framework.authentication import *


class QueryTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.query_params.get('token', None)
        if token:
            return None, token
        else:
            raise exceptions.AuthenticationFailed('Not Found Token From Query Params!')
