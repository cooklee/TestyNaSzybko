import pytest
from django.contrib.auth.models import Permission, User

from books_app.models import Author


@pytest.fixture
def author():
    return Author.objects.create(first_name='Test', last_name='Testowy')


@pytest.fixture
def authors():
    n = 5
    lst = []
    for x in range(n):
        lst.append(Author.objects.create(first_name=x, last_name=x))
    return lst


@pytest.fixture
def user_with_permission():
    p = Permission.objects.get(codename='add_book')
    u = User.objects.create(username='b')
    u.user_permissions.add(p)
    return u



