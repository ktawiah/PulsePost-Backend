from djoser.social.views import ProviderAuthView
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from settings.base import Base

from ..renderers import AccountsRenderer
from .serializers import CustomTokenObtainPairSerializer


class CustomUserViewSet(UserViewSet):
    renderer_classes = [AccountsRenderer]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    renderer_classes = [AccountsRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            access_token = response.data.get("access")
            refresh_token = response.data.get("refresh")

        response.set_cookie(
            key="access",
            value=access_token,
            httponly=Base.AUTH_COOKIE_HTTPONLY,
            samesite=Base.AUTH_COOKIE_SAMESITE,
            max_age=Base.AUTH_COOKIE_ACCESS_MAX_AGE,
            path=Base.AUTH_COOKIE_PATH,
            secure=Base.AUTH_COOKIE_SECURE,
        )

        response.set_cookie(
            key="refresh",
            value=refresh_token,
            httponly=Base.AUTH_COOKIE_HTTPONLY,
            samesite=Base.AUTH_COOKIE_SAMESITE,
            max_age=Base.AUTH_COOKIE_REFRESH_MAX_AGE,
            path=Base.AUTH_COOKIE_PATH,
            secure=Base.AUTH_COOKIE_SECURE,
        )

        return response


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        refresh_token = request.COOKIES.get("refresh")

        if refresh_token:
            request.data["refresh"] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            access_token = response.data.get("access")
            response.set_cookie(
                key="access",
                value=access_token,
                httponly=Base.AUTH_COOKIE_HTTPONLY,
                samesite=Base.AUTH_COOKIE_SAMESITE,
                max_age=Base.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=Base.AUTH_COOKIE_PATH,
                secure=Base.AUTH_COOKIE_SECURE,
            )

        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        access_token = request.COOKIES.get("access")

        if access_token:
            request.data["token"] = access_token

        response = super().post(request, *args, **kwargs)

        return response


class LogoutView(APIView):
    serializer_class = None

    def post(self, request: Request, *args, **kwargs) -> Response:
        response = Response(status=status.HTTP_204_NO_CONTENT)

        if response:
            response.delete_cookie("access")
            response.delete_cookie("refresh")

        return response


class CustomProviderAuthView(ProviderAuthView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            access_token = response.data.get("access")
            refresh_token = response.data.get("refresh")

        response.set_cookie(
            key="access",
            value=access_token,
            httponly=Base.AUTH_COOKIE_HTTPONLY,
            samesite=Base.AUTH_COOKIE_SAMESITE,
            max_age=Base.AUTH_COOKIE_ACCESS_MAX_AGE,
            path=Base.AUTH_COOKIE_PATH,
            secure=Base.AUTH_COOKIE_SECURE,
        )

        response.set_cookie(
            key="refresh",
            value=refresh_token,
            httponly=Base.AUTH_COOKIE_HTTPONLY,
            samesite=Base.AUTH_COOKIE_SAMESITE,
            max_age=Base.AUTH_COOKIE_REFRESH_MAX_AGE,
            path=Base.AUTH_COOKIE_PATH,
            secure=Base.AUTH_COOKIE_SECURE,
        )

        return response
