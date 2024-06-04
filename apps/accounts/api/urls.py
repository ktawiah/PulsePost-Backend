from django.urls import path

from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    CustomUserViewSet,
    LogoutView,
)

# from djoser.views import UserViewSet


urlpatterns = [
    path(
        "activate/",
        CustomUserViewSet.as_view({"post": "activation"}),
        name="account_activate",
    ),
    path("users/", CustomUserViewSet.as_view({"get": "list"}), name="users_list"),
    path(
        "users/me/",
        CustomUserViewSet.as_view({"get": "me"}),
        name="user_detail",
    ),
    path(
        "register/",
        CustomUserViewSet.as_view({"post": "create"}),
        name="account_register",
    ),
    path(
        "reset-password/",
        CustomUserViewSet.as_view({"post": "reset_password"}),
        name="reset_password",
    ),
    path(
        "reset-password/confirm/",
        CustomUserViewSet.as_view({"post": "reset_password_confirm"}),
        name="reset_password_confirm",
    ),
    path(
        "login/",
        CustomTokenObtainPairView.as_view(),
        name="account_login",
    ),
    path(
        "refresh/",
        CustomTokenRefreshView.as_view(),
        name="account_refresh",
    ),
    path(
        "verify/",
        CustomTokenVerifyView.as_view(),
        name="account_verify",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="account_logout",
    ),
    path(
        "oauth/<str:provider>/",
        CustomProviderAuthView.as_view(),
    ),
]
