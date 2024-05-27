import pytest
from faker import Faker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

fake = Faker()


@pytest.mark.django_db
def test_account_registration_success(api_client, registration_endpoint):
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
    print(response.json())
    assert response.status_code == HTTP_201_CREATED
    assert response.json().get("email") is not None
    assert response.json().get("first_name") is not None
    assert response.json().get("last_name") is not None
