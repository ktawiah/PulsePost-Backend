from django.core.management.utils import (
    get_random_secret_key,
)

from .base import Base


class Production(Base):
    # For psql when in production
    SOCIAL_AUTH_JSONFIELD_ENABLED = True

    DEBUG = False

    SECRET_KEY = get_random_secret_key()

    # TODO: Add specific domains when in production
    # CORS_ALLOWED_ORIGINS =
    # ALLOWED_HOSTS =
