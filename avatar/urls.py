from django.urls import path
from . import views


urlpatterns = [
    path('', views.AvatarCreateView.as_view(), name='avatar'),
]