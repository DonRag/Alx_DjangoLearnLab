from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, ListView, CreateView, DetailView, UpdateView, DeleteView , BookListView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/list/', ListView.as_view(), name='book-list'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/detail/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Token authentication endpoint
]