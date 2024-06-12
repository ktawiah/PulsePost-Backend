import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

fake = Faker()


@pytest.mark.django_db
def test_user_creation(api_client, user_data):
    url = reverse("account_register")
    response = api_client.post(
        path=url,
        data={
            "email": user_data.get("email"),
            "first_name": user_data.get("first_name"),
            "last_name": user_data.get("last_name"),
            "password": user_data.get("password"),
            "re_password": user_data.get("password"),
        },
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.get("id") is not None


@pytest.mark.django_db
def test_user_creation_password_mismatch(api_client, user_data):
    url = reverse("account_register")
    response = api_client.post(
        path=url,
        data={
            "email": user_data.get("email"),
            "first_name": user_data.get("first_name"),
            "last_name": user_data.get("last_name"),
            "password": user_data.get("password"),
            "re_password": fake.password(),
        },
        format="json",
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_login_success(api_client, user_data, create_user):
    create_user()
    url = reverse("account_login")
    response = api_client.post(
        path=url,
        data={
            "email": user_data.get("email"),
            "password": user_data.get("password"),
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("access") is not None
    assert response.data.get("refresh") is not None
    assert response.data.get("id") is not None


@pytest.mark.django_db
def test_login_with_wrong_password(api_client, user_data, create_user):
    create_user()
    url = reverse("account_login")
    response = api_client.post(
        path=url,
        data={
            "email": user_data.get("email"),
            "password": fake.password(),
        },
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_refresh_success(api_client, create_user):
    url = reverse("account_refresh")
    user = create_user()
    refresh_token = RefreshToken.for_user(user)
    response = api_client.post(
        path=url,
        data={
            "refresh": str(refresh_token),
        },
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_refresh_wrong_refresh_token(api_client, create_user):
    url = reverse("account_refresh")
    create_user()
    response = api_client.post(
        path=url,
        data={
            "refresh": fake.uuid4(),
        },
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_verify_success(api_client, create_user):
    user = create_user()
    url = reverse("account_verify")
    access_token = RefreshToken.for_user(user).access_token
    response = api_client.post(
        path=url,
        data={
            "token": str(access_token),
        },
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_verify_with_wrong_access_token(api_client, create_user, user_data):
    create_user()
    url = reverse("account_verify")
    response = api_client.post(
        path=url,
        data={
            "token": fake.uuid4(),
        },
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_user_detail_endpoint(api_client, create_user):
    user = create_user()
    refresh_token = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh_token.access_token}")
    url = reverse("user_detail")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data.get("id") is not None
    assert response.data.get("email") is not None
