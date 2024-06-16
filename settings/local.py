import os

from .base import Base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Base):
    DEBUG = True
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
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
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

    CORS_ALLOW_ALL_ORIGINS = True
