import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.fixture
def api_client():
    return APIClient(enforce_csrf_checks=True)


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


@pytest.fixture
def verify_endpoint():
    url = reverse("jwt_verify")
    return url


@pytest.fixture
def logout_endpoint():
    url = reverse("account_logout")
    return url


# TODO: Update base url when in production
base_url = "http://localhost:8000"


@pytest.fixture
def google_auth_endpoint():
    url = f"{base_url}/api/auth/o/google-oauth2/"
    return url


@pytest.fixture
def github_auth_endpoint():
    url = f"{base_url}/api/auth/o/github/"
    return url
