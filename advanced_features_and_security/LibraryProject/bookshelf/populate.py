# Import the models
from bookshelf.models import Author, Book, Library, Librarian, CustomUser, UserProfile
from django.contrib.auth.models import Permission
from django.db import IntegrityError

# Add Custom Users
James = CustomUser.objects.create_superuser(
    username="admin",
    email="admin@example.com",
    password="adminpassword",
    date_of_birth="1998-10-01",
    profile_photo=None  # Assuming no initial profile picture
)

Jane = CustomUser.objects.create_user(
    username="member1",
    email="user@example.com",
    password="userpassword",
    date_of_birth="1992-06-15",
    profile_photo=None
)

# Create User Profiles
UserProfile.objects.create(user=James, role='Admin')
UserProfile.objects.create(user=Jane, role='Member')

# Add authors
authors = [
    "George Orwell", "Harper Lee", "Jane Austen", "F. Scott Fitzgerald",
    "Herman Melville", "J.K. Rowling", "J.R.R. Tolkien",
    "George R.R. Martin", "Agatha Christie", "Mark Twain"
]
author_objects = [Author.objects.create(name=author) for author in authors]

# Add books for each author
books_data = [
    ("1984", author_objects[0]),
    ("Animal Farm", author_objects[0]),
    ("Homage to Catalonia", author_objects[0]),
    ("To Kill a Mockingbird", author_objects[1]),
    ("Go Set a Watchman", author_objects[1]),
    ("Pride and Prejudice", author_objects[2]),
    ("Sense and Sensibility", author_objects[2]),
    ("Emma", author_objects[2]),
    ("The Great Gatsby", author_objects[3]),
    ("Tender is the Night", author_objects[3]),
    ("This Side of Paradise", author_objects[3]),
    ("Moby Dick", author_objects[4]),
    ("Bartleby, the Scrivener", author_objects[4]),
    ("Billy Budd, Sailor", author_objects[4]),
    ("Harry Potter and the Philosopher's Stone", author_objects[5]),
    ("Harry Potter and the Chamber of Secrets", author_objects[5]),
    ("The Hobbit", author_objects[6]),
    ("The Lord of the Rings", author_objects[6]),
    ("A Game of Thrones", author_objects[7]),
    ("A Clash of Kings", author_objects[7]),
    ("Murder on the Orient Express", author_objects[8]),
    ("And Then There Were None", author_objects[8]),
    ("The Adventures of Tom Sawyer", author_objects[9]),
    ("The Adventures of Huckleberry Finn", author_objects[9]),
]
book_objects = [Book.objects.create(title=title, author=author) for title, author in books_data]

# Add libraries
library_names = ["Chiron Library", "Veyron Library", "Divo Library", "Centodieci Library", "Bolide Library"]
libraries = [Library.objects.create(name=name) for name in library_names]

# Add books to libraries
libraries[0].books.add(Book.objects.get(title="1984"))
libraries[0].books.add(Book.objects.get(title="The Great Gatsby"))
libraries[1].books.add(Book.objects.get(title="Pride and Prejudice"))
libraries[1].books.add(Book.objects.get(title="To Kill a Mockingbird"))
libraries[2].books.add(Book.objects.get(title="The Adventures of Huckleberry Finn"))
libraries[2].books.add(Book.objects.get(title="Murder on the Orient Express"))
libraries[3].books.add(Book.objects.get(title="Harry Potter and the Philosopher's Stone"))
libraries[3].books.add(Book.objects.get(title="The Lord of the Rings"))
libraries[4].books.add(Book.objects.get(title="A Game of Thrones"))
libraries[4].books.add(Book.objects.get(title="Moby Dick"))

# Add librarians
librarian_names = ["Zinedine Zidane", "Raúl González", "Iker Casillas", "Cristiano Ronaldo", "Alfredo Di Stéfano"]
librarian_objects = [Librarian.objects.create(name=name, library=libraries[i]) for i, name in enumerate(librarian_names)]

# Assign a permission to a user
try:
    permission = Permission.objects.get(codename='can_add_book')
    Jane.user_permissions.add(permission)
except Permission.DoesNotExist:
    print("Permission 'can_add_book' does not exist.")

# Testing Queries (optional, for verification)
books_in_chiron_library = libraries[0].books.all()
print([book.title for book in books_in_chiron_library])

# Integrity Checks (optional)
try:
    Book.objects.create(title="Duplicate Book", author=author_objects[0])
except IntegrityError as e:
    print("Integrity error:", e)

# Additional Library Data (optional)
libraries[0].description = "A serene environment for classic literature lovers."
libraries[0].location = "123 Chiron St, Fiction City"
libraries[0].save()
