import pytest

from mainblog.forms import PostUpdateForm, PostCreateForm
from mainblog.models import Post, Role
from users.forms import UserRegistrationForm
from users.models import Account
from django.contrib.auth.models import User


@pytest.fixture
def user_data():
    return {"username": "Alex228", "email": "alex@mail.ru", "password": "qwerty123", "password2": "qwerty123",
            "first_name": "alex", "last_name": "alekseev"}


@pytest.fixture
def post_data():
    return {"title": "Test_Title", "text": "test_text here"}


@pytest.mark.django_db
def test_user_reg(user_data):
    assert UserRegistrationForm(data=user_data).is_valid()


@pytest.mark.django_db
def test_post_create(post_data):
    assert PostCreateForm(data=post_data).is_valid()


@pytest.mark.django_db
def test_post_update(post_data):
    assert PostUpdateForm(data=post_data).is_valid()
