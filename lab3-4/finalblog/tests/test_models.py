import pytest
from mainblog.models import Post, Role
from users.models import Account
from django.contrib.auth.models import User


@pytest.fixture
def role():
    return Role.objects.create(name="Poser")


@pytest.fixture
def user(role):
    return User.objects.create_user(username="Alex", email="alex@mail.ru", password="qwerty123", role=role)


@pytest.fixture
def account(user):
    return Account.objects.create(user=user, phone='+375291234567')


@pytest.fixture
def post(user):
    return Post.objects.create(author=user, title="Title", text="Prosto text")


@pytest.mark.django_db
def test_create_post(post):
    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_create_user(post):
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_role(user, role):
    assert user.role == role


@pytest.mark.django_db
def test_post_type(post):
    assert isinstance(post, Post)


@pytest.mark.django_db
def test_owner(post, user):
    assert post.author == user


@pytest.mark.django_db
def test_role(role, user):
    assert role.name == user.role.name


@pytest.mark.django_db
def test_account(account, user, post):
    assert account.user == user
    assert post.author == account.user


@pytest.mark.django_db
def test_str(post):
    assert post.title == str(post)

@pytest.mark.django_db
def test_account_str(account, user):
    assert str(account) == user.first_name + ' ' + user.last_name
