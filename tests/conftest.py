import pytest
from rest_framework.test import APIClient

from apps.accounts.models import User


@pytest.fixture
def user_data():
    return {
        "email": "testuser123@pulsepost.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "!uth892ngh28*99#",
        "is_active": True,
        "is_staff": False,
    }


@pytest.fixture
def create_user(user_data):
    def _create_user():
        user = User.objects.create_user(**user_data)
        return user

    return _create_user


@pytest.fixture
def api_client():
    return APIClient()
