from django.urls import include, re_path


websocket_urlpatterns = [
    re_path(r'ws/users/', include('users.routing')),
]