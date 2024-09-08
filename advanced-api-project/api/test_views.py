from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        # Initialize the API client
        self.client = APIClient()

        # Create a user for the 'owner' field
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create book objects associated with the user
        self.book1 = Book.objects.create(
            title='Test Book 1',
            author='Test Author 1',
            publication_year=2021,
            owner=self.user
        )
        self.book2 = Book.objects.create(
            title='Test Book 2',
            author='Test Author 2',
            publication_year=2022,
            owner=self.user
        )

        # Log in as the user for API testing
        self.client.login(username='testuser', password='testpassword')

    def test_list_books(self):
        # Test listing books with proper authentication
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        # Test creating a new book
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2023,
            'owner': self.user.id  # Reference to the user ID
        }
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        # Test updating an existing book
        data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2024
        }
        response = self.client.put(f'/api/books/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        # Test filtering books by author
        response = self.client.get('/api/books/', {'author': 'Test Author 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    def test_search_books(self):
        # Test searching for books by title or author
        response = self.client.get('/api/books/', {'search': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    def test_order_books_by_publication_year(self):
        # Test ordering books by publication year
        response = self.client.get('/api/books/', {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')
        self.assertEqual(response.data[1]['title'], 'Test Book 2')

    def test_unauthorized_access(self):
        # Log out the current user
        self.client.logout()

        # Attempt to access book list without authentication
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
