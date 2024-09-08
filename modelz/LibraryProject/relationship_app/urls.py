from django.urls import path
from .views import list_books, LibraryDetailView  # Import the views
from .views import UserRegisterView, UserLoginView, UserLogoutView
from .views import admin_view, librarian_view, member_view
from . import views

urlpatterns = [
    # Route for the function-based view to list all books
    path('books/', list_books, name='list_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    
    # Route for the class-based view to display library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),  # URL pattern for the profile page
    
    # Custom role-based views with updated paths
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),
]























"""

from django.contrib.auth.models import User
from relationship_app.models import UserProfile

# Create the first user
user1 = User.objects.create_user('Jack', 'jack@example.com', 'password')

# Retrieve the associated UserProfile
profile1 = UserProfile.objects.get(user=user1)

# Set the role to 'Admin'
profile1.role = 'Admin'
profile1.save()

# Create the second user
user2 = User.objects.create_user('John', 'john@example.com', 'password')

# Retrieve the associated UserProfile
profile2 = UserProfile.objects.get(user=user2)

# Set the role to 'Librarian'
profile2.role = 'Librarian'
profile2.save()

# Create the third user
user3 = User.objects.create_user('Jane', 'jane@example.com', 'password')

# Retrieve the associated UserProfile
profile3 = UserProfile.objects.get(user=user3)

# Set the role to 'Member'
profile3.role = 'Member'
profile3.save()

"""