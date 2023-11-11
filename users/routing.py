from django.urls import re_path, path
from .consumers import TokenAuthConsumer

websocket_urlpatterns = [
    re_path(r'', TokenAuthConsumer.as_asgi(), name='auth'),
]