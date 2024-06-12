import pytest
from faker import Faker
from rest_framework.test import APIClient

from apps.accounts.models import User
from apps.posts.models import Post

fake = Faker()


@pytest.fixture
def api_client():
    return APIClient()


# Accounts
@pytest.fixture
def user_data():
    return {
        "email": fake.email(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "password": fake.password(),
        "is_active": True,
        "is_staff": False,
    }


@pytest.fixture
def create_user(user_data):
    def _create_user():
        user = User.objects.create_user(**user_data)
        return user

    return _create_user


# Posts
@pytest.fixture
def post_data(create_user):
    user = create_user()
    return {
        "title": fake.sentence(),
        "content": fake.text(),
        "status": "published",
        "user": user,
    }


@pytest.fixture
def create_post(post_data):
    def _create_post():
        post = Post.objects.create(**post_data)
        return post

    return _create_post
