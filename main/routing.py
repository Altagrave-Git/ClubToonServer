from django.urls import re_path
from users.routing import websocket_urlpatterns as users_urlpatterns


websocket_urlpatterns = users_urlpatterns