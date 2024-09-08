from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework 
from rest_framework import filters


# ViewSet for Author model
class AuthorViewSet(viewsets.ModelViewSet):
    # Prefetch related books to reduce database queries for each author
    queryset = Author.objects.all().prefetch_related('books')
    serializer_class = AuthorSerializer
    
    # Overriding the default queryset to allow filtering by 'name' via query params
    def get_queryset(self):
        queryset = self.queryset
        # Check if 'name' is provided in query params to filter authors by name (case-insensitive)
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset
    

# ViewSet for Book model
class BookViewSet(viewsets.ModelViewSet):
    # Set the default queryset to retrieve all books
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Overriding the default queryset to allow filtering by 'author' name via query params
    def get_queryset(self):
        queryset = self.queryset
        # Check if 'author' is provided in query params to filter books by author's name (case-insensitive)
        author_name = self.request.query_params.get('author', None)
        if author_name is not None:
            queryset = queryset.filter(author__name__icontains=author_name)
        return queryset


# API View for listing and creating books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Serialize the books data
    
    # Add filter, search, and ordering functionality to the view
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']  # Allow filtering by author
    search_fields = ['title', 'author']  # Allow search by book title and author
    ordering_fields = ['publication_year']  # Allow ordering by publication year
    

# API View for listing all books with read-only permissions for unauthenticated users
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Serialize the books data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read access to unauthenticated users


# API View for creating a new book, authentication required
class CreateView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can create
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Serialize the books data


# API View for retrieving, updating, and deleting a book (full CRUD), allows read access to unauthenticated users
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Serialize the books data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read access to unauthenticated users


# API View for updating a book, authentication required
class UpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can update
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Serialize the books data


# API View for deleting a book, authentication required
class DeleteView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Serialize the books data
