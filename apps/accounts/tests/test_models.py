from .factories import UserFactory


def test_single_user_create():
    user = UserFactory.build()
    assert user is not None
    assert user.email is not None
    assert user.id is not None


def test_password_properly_hashed():
    user = UserFactory.build(password="testpassword123")
    assert user.password is not None
    assert user.password.startswith("pbkdf2")
    assert user.check_password("testpassword123")


def test_batch_user_create():
    user_list = UserFactory.build_batch(10)
    assert len(user_list) == 10
