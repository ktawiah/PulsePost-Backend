import pytest
from rest_framework import status


@pytest.mark.django_db
def test_google_auth_get_success(api_client, google_auth_endpoint):
    response = api_client.get(
        path=f"{google_auth_endpoint}?redirect_uri=http://localhost:3000/api/auth/google/callback",
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("authorization_url") is not None


@pytest.mark.django_db
def test_google_auth_wrong_redirect_uri(api_client, google_auth_endpoint):
    response = api_client.get(
        path=f"{google_auth_endpoint}?redirect_uri=http://localhost:3000/api/auth/google",
        format="json",
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_github_auth_get_success(api_client, github_auth_endpoint):
    response = api_client.get(
        path=f"{github_auth_endpoint}?redirect_uri=http://localhost:3000/api/auth/google/callback",
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("authorization_url") is not None


@pytest.mark.django_db
def test_github_auth_wrong_redirect_uri(api_client, github_auth_endpoint):
    response = api_client.get(
        path=f"{github_auth_endpoint}?redirect_uri=http://localhost:3000/api/auth/google",
        format="json",
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
