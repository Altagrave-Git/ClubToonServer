from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

from rest_framework import status, permissions, parsers
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer, AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return super(LoginView, self).post(request, format=None)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        if User.objects.filter(email=request.data['email']).exists():
            return Response(data={'error': 'Email is already taken.'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = user.auth_token_set.all()[0]
            login(request, user)

            data = {
                'expiry': token.expiry,
                'token': token.digest,
                'user': serializer.data
            }

            return Response(data=data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
