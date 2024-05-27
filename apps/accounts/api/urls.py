from django.urls import path, include
from .views import CustomTokenObtainPairView

urlpatterns = [
    path("", include("djoser.urls")),
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt_create"),
]
