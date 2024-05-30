from django.urls import path, include
from django.contrib.auth.views import LogoutView

# from rest_framework.routers import DefaultRouter

from . import views

app_name = "blog"

# router = DefaultRouter()
# router.register("user", views.LoginView, basename="user")

urlpatterns = [
    path("", views.blog, name="blog"),
    path("login/", views.login, name="login"),
    path("registration/", views.register, name="registration"),
    path("profile", views.profile, name="profile"),
    # TOKEN
    path("token/", views.TokenObtainPairView.as_view()),
    path("token/refresh/", views.TokenRefreshView.as_view()),
    # USER
    path("api/registration/", views.RegistrationView.as_view({"post": "create"})),
    path("api/user/", views.UserView.as_view({"get": "get_current_user"})),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    # path("api/login/", views.LoginView.as_view({"get": "get_current_user"})),
    # CARD
    path("api/card/", views.CardGetAllView.as_view({"get": "list"}), name="CardAll"),
    # API
    # path("api", include(router.urls)),
]
