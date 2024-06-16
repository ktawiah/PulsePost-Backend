from django.core.management.utils import get_random_secret_key

from .base import Base


class Production(Base):
    # For psql when in production
    SOCIAL_AUTH_JSONFIELD_ENABLED = True

    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql",
    #         "NAME": "postgres",
    #         "USER": "postgres",
    #         "PASSWORD": "postgres",
    #         "HOST": "localhost",
    #         "PORT": "5432",
    #         "ATOMIC_REQUESTS": True,
    #         "CONN_MAX_AGE": 630,
    #     },
    # }

    DEBUG = False

    SECRET_KEY = get_random_secret_key()

    # TODO: Add specific domains when in production
    # CORS_ALLOWED_ORIGINS =
    # ALLOWED_HOSTS =
