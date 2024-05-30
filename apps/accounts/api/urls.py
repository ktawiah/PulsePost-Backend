from django.urls import path, include
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
    CustomProviderAuthView,
)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="account_login"),
    path("refresh/", CustomTokenRefreshView.as_view(), name="account_refresh"),
    path("verify/", CustomTokenVerifyView.as_view(), name="account_verify"),
    path("logout/", LogoutView.as_view(), name="account_logout"),
    path("oauth/<str:provider>/", CustomProviderAuthView.as_view(), name=""),
]
