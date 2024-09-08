from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f'{self.user.username} - {self.role}'

# # Signal to create or update the UserProfile when a User is created or updated
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     else:
#         # Update the profile if it already exists
#         instance.userprofile.save()

# Define other models...



# Define the Author model, which will store information about different authors.
class Author(models.Model):
    # The name of the author, stored as a character field with a maximum length of 100 characters.
    name = models.CharField(max_length=100)
    
    # String representation of the Author object to return the author's name for easy identification in the admin interface and shell.
    def __str__(self) -> str:
        return self.name

# Define the Book model, which will store information about different books.
class Book(models.Model):
    # The title of the book, stored as a character field with a maximum length of 200 characters.
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)  # Default ISBN, usually it's a placeholder
    # publication_date = models.DateField(default=date.today)  # Default to today's date
    # number_of_pages = models.IntegerField(default=0)  # Default to 0 pages
    
    """
    ForeignKey establishes a many-to-one relationship with the Author model.
    Each book is linked to one author, but an author can write many books.
    The on_delete=models.CASCADE option means that if an author is deleted, all their books will also be deleted.
    The related_name='books' allows us to access all books written by an author using author.books.all().
    """
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, 
        related_name='books'
    )
    
    class Meta:
        permissions = [
        ("can_add_book","Can add book"),   
        ("can_change_book","Can change book"),   
        ("can_delete_book","Can delete book"),   
        ]
    
    # String representation of the Book object to return the book's title and author for easy identification.
    def __str__(self) -> str:
        return f"{self.title} by {self.author.name}"

# Define the Library model, which will store information about different libraries.
class Library(models.Model):
    # The name of the library, stored as a character field with a maximum length of 200 characters.
    name = models.CharField(max_length=200)
    
    """
    ManyToManyField establishes a many-to-many relationship with the Book model.
    A library can have many books, and a book can be present in many libraries.
    The related_name='libraries' allows us to access all libraries that contain a particular book using book.libraries.all().
    """
    books = models.ManyToManyField(
        Book, related_name='libraries'
    )
    
    # String representation of the Library object to return the library's name for easy identification.
    def __str__(self) -> str:
        return self.name

# Define the Librarian model, which will store information about librarians.
class Librarian(models.Model):
    # The name of the librarian, stored as a character field with a maximum length of 100 characters.
    name = models.CharField(max_length=100)
    
    """
    OneToOneField establishes a one-to-one relationship with the Library model.
    Each librarian is associated with one library, and each library has one librarian.
    The on_delete=models.CASCADE option means that if a library is deleted, the associated librarian is also deleted.
    """
    library = models.OneToOneField(
        Library, on_delete=models.CASCADE
    )
    
    # String representation of the Librarian object to return the library's name followed by 'Librarian' for easy identification.
    def __str__(self):
        return f"{self.library.name} - Librarian"
