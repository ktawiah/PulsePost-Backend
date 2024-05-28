from django.urls import path, include
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
)

urlpatterns = [
    path("", include("djoser.urls")),
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", CustomTokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", CustomTokenVerifyView.as_view(), name="jwt_verify"),
]
