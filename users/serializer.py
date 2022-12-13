from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User

class UserSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=127)
    password = serializers.CharField(max_length=127, write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):

        if not validated_data["is_employee"]:
            user_obj = User.objects.create_user(**validated_data)
            return user_obj
        
        user_obj = User.objects.create_superuser(**validated_data)

        return user_obj

    
    def validate_username(self,username):
        username_already_exists = User.objects.filter(username = username).exists()

        if username_already_exists:
            raise serializers.ValidationError(detail="username already taken.")
        return username

    def validate_email(self, email):
        email_already_exists = User.objects.filter(email = email).exists()
        if email_already_exists:
            raise serializers.ValidationError(detail= "email already registered.")
        return email    


class JWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser

        return token