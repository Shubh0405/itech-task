from rest_framework import serializers
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib import auth

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email','phone_number', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        phone_number = attrs.get('phone_number', '')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=50, min_length=8,write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email','password','tokens']

    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        user = auth.authenticate(email=email,password=password)

        print(email)
        print(password)
        print(user)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')

        return {
            'email': user.email,
            'tokens': user.tokens
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
