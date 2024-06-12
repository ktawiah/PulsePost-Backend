import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

fake = Faker()


def authenticate_user(user, api_client):
    refresh_token = RefreshToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh_token.access_token}")


@pytest.mark.django_db
def test_create_post(api_client, post_data):
    user = post_data.get("user")
    authenticate_user(user, api_client)
    url = reverse("post_list")
    response = api_client.post(
        path=url,
        data={
            "title": post_data.get("title"),
            "content": post_data.get("content"),
            "user": user.id,
        },
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_get_created_post(create_post, api_client):
    post = create_post()
    user = post.user
    authenticate_user(user, api_client)
    url = reverse("post_detail", kwargs={"pk": post.id})
    response = api_client.get(path=url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_all_posts(api_client, create_post):
    post = create_post()
    create_post()
    create_post()
    create_post()
    create_post()
    authenticate_user(post.user, api_client)
    url = reverse("post_list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_delete_post(create_post, api_client):
    post = create_post()
    authenticate_user(post.user, api_client)
    url = reverse("post_detail", kwargs={"pk": post.id})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_update_post(create_post, api_client):
    post = create_post()
    authenticate_user(post.user, api_client)
    updated_data = {
        "title": fake.sentence(),
        "content": fake.text(),
        "status": "draft",
        "user": post.user.id,
    }
    url = reverse("post_detail", kwargs={"pk": post.id})
    response = api_client.put(
        path=url,
        data=updated_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert updated_data.get("title") == response.data.get("title")


@pytest.mark.django_db
def test_partial_update_post(create_post, api_client):
    post = create_post()
    authenticate_user(post.user, api_client)
    updated_data = {
        "title": fake.sentence(),
        "status": "draft",
        "user": post.user.id,
    }
    url = reverse("post_detail", kwargs={"pk": post.id})
    response = api_client.patch(
        path=url,
        data=updated_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert updated_data.get("title") == response.data.get("title")
