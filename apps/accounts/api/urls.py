from django.urls import path, include
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    CustomProviderAuthView,
)
from djoser.views import UserViewSet

urlpatterns = [
    path(
        "activate/",
        UserViewSet.as_view({"post": "activation"}),
        name="account_activate",
    ),
    path("users/", UserViewSet.as_view({"get": "list"}), name="users_list"),
    path("users/me/", UserViewSet.as_view({"get": "me"}), name="user_detail"),
    path("register/", UserViewSet.as_view({"post": "create"}), name="account_register"),
    path(
        "reset-password/",
        UserViewSet.as_view({"post": "reset_password"}),
        name="reset_password",
    ),
    path(
        "reset-password/confirm/",
        UserViewSet.as_view({"post": "reset_password_confirm"}),
        name="reset_password_confirm",
    ),
    path("login/", CustomTokenObtainPairView.as_view(), name="account_login"),
    path("refresh/", CustomTokenRefreshView.as_view(), name="account_refresh"),
    path("verify/", CustomTokenVerifyView.as_view(), name="account_verify"),
    path("logout/", LogoutView.as_view(), name="account_logout"),
    path("oauth/<str:provider>/", CustomProviderAuthView.as_view(), name=""),
]
