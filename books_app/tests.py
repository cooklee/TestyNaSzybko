from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

import pytest

from books_app.forms import AddAuthorForm
from books_app.models import Author, Book


def test_index_view_return_200():
    clinet = Client()
    url = reverse('index')
    response = clinet.get(url)  # wpisali w adresie przegladrki url
    assert response.status_code == 200


@pytest.mark.parametrize('n, numbers', (
        (1, [0]),
        (2, [0, 1]),
        (3, [0, 1, 2]),
        (4, [0, 1, 2, 3]),
        (5, [0, 1, 2, 3, 4])
))
def test_numbers_view_numbers_in_context(n, numbers):
    client = Client()
    url = reverse('numbers', kwargs={'n': n})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['numbers'] == numbers


def test_add_author_get():
    client = Client()
    url = reverse('add_author')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddAuthorForm)

@pytest.mark.django_db
def test_add_author_post():
    client = Client()
    url = reverse('add_author')
    data = {
        'first_name': 'slawek',
        'last_name': 'bo'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Author.objects.get(**data)

@pytest.mark.django_db
def test_list_author(authors):
    client = Client()
    url = reverse('list_author')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['authors'].count() == len(authors)
    for item in authors:
        assert item in response.context['authors']


@pytest.mark.django_db
def test_add_book_lack_of_permission(author):
    u = User.objects.create(username='ala')
    client = Client()
    client.force_login(u)
    url = reverse('add_book')
    data = {
        'title':'ala ma kota',
        'author':author.id
    }
    response = client.post(url,data)
    assert response.status_code == 403
    # Book.objects.get(title='ala ma kota', author=author)

@pytest.mark.django_db
def test_add_book_lack_of_permission(author, user_with_permission):

    client = Client()
    client.force_login(user_with_permission)
    url = reverse('add_book')
    data = {
        'title':'ala ma kota',
        'author':author.id
    }
    response = client.post(url,data)
    assert response.status_code ==302
    Book.objects.get(title='ala ma kota', author=author)





