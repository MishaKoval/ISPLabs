import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from mainblog.forms import PostCreateForm, PostUpdateForm
from mainblog.models import Post
from users.forms import UserRegistrationForm
from users.models import Account

User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create_user(username="sanek111", password="qwerty123", email="sanchez@mail.ru")


@pytest.fixture
def account(user):
    return Account.objects.create(user=user, phone="1234")


@pytest.fixture
def post(user):
    return Post.objects.create(title="sanek_Title", text="sanya na meste", author=user)


@pytest.mark.parametrize('param', [
    ('register'),
    ('login'),
    ('logout'),
    ('create_post'),
])
def test_render_views(client, param):
    temp_url = reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200 or resp.status_code == 302


@pytest.mark.django_db
def test_register(client):
    data = {"username": "Alex228", "email": "alex@mail.ru", "password": "qwerty123", "password2": "qwerty123",
            "first_name": "alex", "last_name": "alekseev"}
    assert UserRegistrationForm(data=data).is_valid()
    client.post("/users/register/", data)
    assert User.objects.filter(username=data["username"])


@pytest.mark.django_db
def test_login(client, user):
    data = {"username": user.username, "password": "qwerty123"}
    client.post("/users/login/", data)
    assert client.post("/users/login/", username=user.username, password="qwerty123")
    assert client.login(username=user.username, password="qwerty123")


@pytest.mark.django_db
def test_detail_user(client, user):
    temp_url = reverse("detail_user", args=(user.id,))
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_update_user(client, user, account):
    temp_url = reverse("update_account", args=(user.id,))
    resp = client.get(temp_url)
    assert resp.status_code == 302

    client.login(username=user.username, password="qwerty123")
    data = {"pk": user.id, "phone": "3523523"}
    response_get = client.get("/users/" + str(user.id) + "/update/")
    assert response_get.status_code == 200

    client.post("/users/" + str(user.id) + "/update/", data=data)
    assert Account.objects.filter(user=user).first().phone == data["phone"]

    response = client.post("/users/" + str(user.id) + "/update/", data={"username": user.username})
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_post(client, user):
    client.login(username=user.username, password="qwerty123")
    resp_get = client.get("/create/")
    assert resp_get.status_code == 200

    data = {"title": "Test_Title", "text": "test_text here"}
    assert PostCreateForm(data=data).is_valid()
    resp_post = client.post("/create/", data)
    assert resp_post.status_code == 302
    assert Post.objects.get(title=data["title"])


@pytest.mark.django_db
def test_delete_post(client, user, post):
    resp_get = client.get("/post/" + post.slug + "/remove")
    assert resp_get.status_code == 404

    client.login(username=user.username, password="qwerty123")
    assert Post.objects.get(author=user).author == post.author

    resp_post = client.post("/post/" + post.slug + "/remove", {"slug": post.slug})
    assert resp_post.status_code == 302
    assert Post.objects.filter(author=user).first() is None


@pytest.mark.django_db
def test_update_post(client, user, post):
    resp_get = client.get("/post/" + post.slug + "/update")
    assert resp_get.status_code == 404

    client.login(username=user.username, password="qwerty123")
    resp_get = client.get("/post/" + post.slug + "/update")
    assert resp_get.status_code == 200

    data = {"title": post.title, "text": "NEW TEXT"}
    assert PostUpdateForm(data=data).is_valid()
    resp_post = client.post("/post/" + post.slug + "/update", data)
    assert resp_post.status_code == 302
    assert Post.objects.filter(author=user).first().text == data["text"]
    assert Post.objects.count() == 1
