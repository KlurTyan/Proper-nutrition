from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer,
    TokenObtainPairSerializer,
)
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from django.core.exceptions import ObjectDoesNotExist

from blog.models import Card, User


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "username"

    def validate(self, *args, **kwargs):
        data = super().validate(*args, **kwargs)

        if not self.user.is_active:
            raise AuthenticationFailed(
                {"detail": f"Пользователь {self.user.username} был деактивирован!"},
                code="user_deleted",
            )

        data["id"] = self.user.id
        data["username"] = self.user.username

        return data


class TokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = RefreshToken(attrs["refresh"])

        try:
            user = User.objects.get(pk=refresh.payload.get("user_id"))
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                {"detail": f"Пользователь был удалён!"}, code="user_does_not_exists"
            )

        if user.blocked:
            raise AuthenticationFailed(
                {"detail": f"Пользователь {user.username} был заблокирован!"},
                code="user_deleted",
            )

        data["id"] = user.id
        data["username"] = user.username

        return data


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        # fields = "__all__"

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', '']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
