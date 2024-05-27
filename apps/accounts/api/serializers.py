from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ..models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom serializer definition for the TokenObtainPairSerializer."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["first_name"] = user.first_name
        token["email"] = user.email
        token["last_name"] = user.last_name
        token["is_active"] = user.is_active
        token["bio"] = user.bio
        token["avatar"] = str(user.avatar)
        token["created_at"] = str(user.created_at)
        token["updated_at"] = str(user.updated_at)

        return token
