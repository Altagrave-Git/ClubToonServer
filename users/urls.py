from django.urls import path
from . import views
from knox.views import LogoutView, LogoutAllView


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logoutall/', LogoutAllView.as_view(), name='logoutall'),
]