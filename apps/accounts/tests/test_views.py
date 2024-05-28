import pytest
from faker import Faker
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from rest_framework.test import force_authenticate
from rest_framework.test import force_authenticate, APIRequestFactory
from .factories import UserFactory
from ..api.views import CustomTokenObtainPairView

fake = Faker()
request_factory = APIRequestFactory()


@pytest.mark.django_db
def test_register_success(api_client, registration_endpoint):
    password = fake.password()
    response = api_client.post(
        path=registration_endpoint,
        data={
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "password": password,
            "re_password": password,
        },
        format="json",
    )
    assert response.status_code == HTTP_201_CREATED
    assert response.json().get("email") is not None
    assert response.json().get("first_name") is not None
    assert response.json().get("last_name") is not None


@pytest.mark.django_db
def test_register_password_mismatch(api_client, registration_endpoint):
    response = api_client.post(
        path=registration_endpoint,
        data={
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "password": fake.password(),
            "re_password": fake.password(),
        },
        format="json",
    )
    assert response.status_code == HTTP_400_BAD_REQUEST
    assert (
        response.json().get("non_field_errors")[0]
        == "The two password fields didn't match."
    )


@pytest.mark.django_db
def test_login_success(api_client, login_endpoint, registration_endpoint):
    password = fake.password()
    reg_user = api_client.post(
        path=registration_endpoint,
        data={
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "password": password,
            "re_password": password,
        },
        format="json",
    )
    response = api_client.post(
        path=login_endpoint,
        data={
            "email": reg_user.json().get("email"),
            "password": password,
        },
        format="json",
    )
    assert response.status_code == HTTP_200_OK
    assert response.json().get("access") is not None
    assert response.json().get("refresh") is not None


@pytest.mark.django_db
def test_login_password_mismatch(api_client, login_endpoint, registration_endpoint):
    password = fake.password()
    reg_user = api_client.post(
        path=registration_endpoint,
        data={
            "email": fake.email(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "password": password,
            "re_password": password,
        },
        format="json",
    )
    response = api_client.post(
        path=login_endpoint,
        data={
            "email": reg_user.json().get("email"),
            "password": fake.password(),
        },
        format="json",
    )
    assert response.status_code == HTTP_401_UNAUTHORIZED
    assert (
        response.json().get("detail")
        == "No active account found with the given credentials"
    )
