from django.contrib.auth.models import update_last_login
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings


class CustomUserSerializer(UserSerializer):

    class Meta(UserCreateSerializer.Meta):
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "bio",
            "avatar",
            "created_at",
            "updated_at",
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom serializer definition for the TokenObtainPairSerializer."""

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        data.update({
            "id": self.user.id,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "is_active": self.user.is_active,
            "bio": self.user.bio,
            "avatar": str(self.user.avatar),
            "created_at": self.user.created_at,
            "updated_at": self.user.updated_at,
        })

        return data
