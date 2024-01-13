from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from avatar.serializers import AvatarSerializer


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, required=False)
    password2 = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'password2', 'username', 'color', 'theme', 'coins', 'avatar', 'is_new']

    def get_avatar(self, obj):
        avatar = obj.avatar.all()
        if avatar.exists():
            return AvatarSerializer(obj.avatar.all()[0]).data
        else:
            return None

    def create(self, validated_data):
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match.")
        
        validated_data.pop('password2')

        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=("Email"),write_only=True)
    password = serializers.CharField( label=("Password"), style={'input_type': 'password'}, trim_whitespace=False, write_only=True)
    token = serializers.CharField(label=("Token"), read_only=True)

    class Meta:
        fields = '__all__'

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
