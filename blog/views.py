from django.shortcuts import render

from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, status
from rest_framework.response import Response

from .models import Card, Profile, User
from .serializer import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
    UserSerializer,
    RegistrationSerializer,
    CardSerializer,
)


def blog(request):
    return render(request, "base.html")


class TokenObtainPairView(TokenObtainSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenObtainPairSerializer

    def get_permissions(self):
        return super().get_permissions()


class TokenRefreshView(TokenRefreshSlidingView):
    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer


def register(request):
    return render(request, "account/register.html")


def login(request):
    return render(request, "account/login.html")


def profile(request):
    return render(request, "profile.html")


class RegistrationView(GenericViewSet, mixins.CreateModelMixin):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class UserView(GenericViewSet, mixins.ListModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_current_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CardGetAllView(GenericViewSet, mixins.ListModelMixin):
    queryset = Card.objects.all()
    permission_classes = [AllowAny]
    serializer_class = CardSerializer
