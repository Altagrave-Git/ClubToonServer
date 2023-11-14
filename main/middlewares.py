from knox.models import AuthToken
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser


@database_sync_to_async
def return_user(token):
    try: user = AuthToken.objects.get(digest=token).user
    except: user = AnonymousUser()
    return user

# token from params => set user scope
class TokenAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        query_string = scope["query_string"]
        query_params = query_string.decode()
        query_dict = parse_qs(query_params)
        token = query_dict["token"][0]
        user = await return_user(token)
        scope["user"] = user
        return await self.app(scope, receive, send)