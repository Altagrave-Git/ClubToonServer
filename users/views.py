from django.contrib.auth.hashers import check_password
from django.contrib import messages
from users.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from users.serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes, renderer_classes, throttle_classes, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication
from rest_framework.authtoken.models import Token



@api_view(["POST"])
def login_view(request):
    if request.method == "POST":
        print(request.data)
        return Response(data={"msg": "received"}, status=status.HTTP_200_OK)

    else:
        return Response(data={"msg": "meh"}, status=status.HTTP_200_OK)
    

@api_view(["POST"])
def loginView(request, *args, **kwargs):
    username = request.POST.get("username")
    password = request.POST.get("password")

    try: user = authenticate(username=username, password=password)
    except: user = None

    if not user:
        return Response({"user_not_found": "There is no user with this username and password !"})
    
    token = Token.objects.get(user=user)
    return Response({"token": token.key,})