import pytest
from faker import Faker
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from .factories import UserFactory

fake = Faker()


@pytest.mark.django_db
def test_register_success(
    api_client,
    registration_endpoint,
):
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
def test_register_password_mismatch(
    api_client,
    registration_endpoint,
):
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
    assert response.json().get("non_field_errors") is not None


import pytest
from django.core import mail
from rest_framework.status import HTTP_200_OK


@pytest.mark.django_db
def test_login_success(api_client, login_endpoint, registration_endpoint):
    password = fake.password()
    email = fake.email()

    # Register the user
    reg_user = api_client.post(
        path=registration_endpoint,
        data={
            "email": email,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "password": password,
            "re_password": password,
        },
        format="json",
    )

    # Ensure registration was successful
    assert reg_user.status_code == HTTP_201_CREATED

    # Simulate email activation
    assert len(mail.outbox) == 1
    activation_email = mail.outbox[0]
    activation_link = [
        word for word in activation_email.body.split() if "http" in word
    ][0]

    # Extract uid and token from the activation link
    activation_url_parts = activation_link.split("/")
    uid = activation_url_parts[-2]
    token = activation_url_parts[-1]

    # Activate the user
    activation_response = api_client.post(
        path=f"/activate/{uid}/{token}/",
        format="json",
    )
    # assert activation_response.status_code == HTTP_204_NO_CONTENT

    # Attempt to log in
    response = api_client.post(
        path=login_endpoint,
        data={
            "email": email,
            "password": password,
        },
        format="json",
    )

    assert response.status_code == HTTP_200_OK
    assert response.json().get("access") is not None
    assert response.json().get("refresh") is not None


@pytest.mark.django_db
def test_login_password_mismatch(
    api_client,
    login_endpoint,
    registration_endpoint,
):
    password = fake.password()
    registered_user = api_client.post(
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
            "email": registered_user.json().get("email"),
            "password": fake.password(),
        },
        format="json",
    )
    assert response.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_refresh_success(
    api_client,
    login_endpoint,
    registration_endpoint,
    refresh_endpoint,
):
    password = fake.password()
    registered_user = api_client.post(
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
    login_response = api_client.post(
        path=login_endpoint,
        data={
            "email": registered_user.json().get("email"),
            "password": password,
        },
        format="json",
    )
    response = api_client.post(
        path=refresh_endpoint,
        data={
            "refresh": login_response.json().get("refresh"),
        },
        format="json",
    )
    assert response.status_code == HTTP_200_OK
    assert response.json().get("access") is not None


@pytest.mark.django_db
def test_verify_success(
    api_client,
    login_endpoint,
    registration_endpoint,
    verify_endpoint,
):
    password = fake.password()
    registered_user = api_client.post(
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
    login_response = api_client.post(
        path=login_endpoint,
        data={
            "email": registered_user.json().get("email"),
            "password": password,
        },
        format="json",
    )
    response = api_client.post(
        path=verify_endpoint,
        data={
            "token": login_response.json().get("access"),
        },
        format="json",
    )
    assert response.status_code == HTTP_200_OK
