from .base import Base
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Base):
    DEBUG = True
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(Base.BASE_DIR, "db.sqlite3"),
        }
    }

    CORS_ALLOW_ALL_ORIGINS = True
