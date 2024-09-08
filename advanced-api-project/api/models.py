from django.db import models  # Importing the models module from Django to define database models
from django.contrib.auth.models import User 

# Model representing an author
class Author(models.Model):
    name = models.CharField(max_length=200)  # Character field to store the author's name, with a maximum length of 200 characters
    
    def __str__(self):
        return self.name  # String representation of the Author model, returning the author's name
    
# Model representing a book
class Book(models.Model):
    title = models.CharField(max_length=255)  # Character field to store the book's title, with a maximum length of 255 characters
    publication_year = models.IntegerField()  # Integer field to store the year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Foreign key linking to the Author model, with a related_name to access books from an author
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title  # String representation of the Book model, returning the book's title
