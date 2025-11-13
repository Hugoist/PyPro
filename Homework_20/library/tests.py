from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # create user and superuser
        self.user = User.objects.create_user(username='user1', password='pass123')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass', email='a@test.com')

        # create tokens
        self.user_token = Token.objects.create(user=self.user)
        self.admin_token = Token.objects.create(user=self.admin)

        # create books
        Book.objects.create(title="Django for Beginners", author="William", genre="Tech", publication_year=2020)
        Book.objects.create(title="Advanced Django", author="William", genre="Tech", publication_year=2021)
        Book.objects.create(title="Poems", author="Anna", genre="Poetry", publication_year=1999)

    def test_list_books_requires_auth(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_create_book(self):
        url = reverse('book-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        data = {"title": "New Book", "author": "Author", "genre": "Fiction", "publication_year": 2000}
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Book.objects.filter(title="New Book").count(), 1)

    def test_filter_by_author(self):
        url = reverse('book-list') + '?author=William'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 2)

    def test_search_title(self):
        url = reverse('book-list') + '?search=django'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(any('Django' in b['title'] or 'django' in b['title'] for b in resp.data['results']))

    def test_delete_only_admin(self):
        book = Book.objects.first()
        url = reverse('book-detail', kwargs={'pk': book.pk})

        # deleting by common user
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 403)  # forbidden

        # deleting by admin
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        resp2 = self.client.delete(url)
        self.assertEqual(resp2.status_code, 204)
