from django.urls import re_path
from channels.routing import URLRouter
from users.routing import websocket_urlpatterns as users_urlpatterns

websocket_urlpatterns = [
    re_path(r'ws/users/', URLRouter(users_urlpatterns)),
]