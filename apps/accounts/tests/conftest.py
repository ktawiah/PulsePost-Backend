import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def registration_endpoint():
    url = reverse("user-list")
    return url


@pytest.fixture
def login_endpoint():
    url = reverse("jwt_create")
    return url


@pytest.fixture
def refresh_endpoint():
    url = reverse("jwt_refresh")
    return url
