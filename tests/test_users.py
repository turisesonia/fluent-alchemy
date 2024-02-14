import pytest
from .models import User


@pytest.fixture
def name(faker):
    return faker.name()


@pytest.fixture
def email(faker):
    return faker.email()


def test_find(email, name):
    u = User.create(
        email=email,
        name=name,
        password="password",
    )

    user = User.find(u.id)

    assert isinstance(user, User)
    assert user.email == email
    assert user.name == name


def test_create(email, name):
    user = User.create(
        email=email,
        name=name,
        password="password",
    )

    assert isinstance(user, User)
    assert user.email == email
    assert user.name == name


def test_save(email, name):
    user = User(
        email=email,
        name=name,
        password="password",
    )

    user.save()

    assert isinstance(user, User)
    assert user.email == email
    assert user.name == name


def test_where(email, name):
    User.create(
        email=email,
        name=name,
        password="password",
    )

    user = User.where(User.email == email).first()

    assert isinstance(user, User)
    assert user.email == email
    assert user.name == name


def test_all(email, name):
    User.create(
        email=email,
        name=name,
        password="password",
    )

    users = User.all()

    assert isinstance(users, list)