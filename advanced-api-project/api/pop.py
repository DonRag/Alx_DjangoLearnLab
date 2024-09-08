# Import the models
from api.models import Author, Book

# List of authors to add
authors_data = [
    {"name": "George Orwell"},
    {"name": "Harper Lee"},
    {"name": "Jane Austen"},
    {"name": "F. Scott Fitzgerald"},
    {"name": "Herman Melville"},
    {"name": "J.K. Rowling"},
    {"name": "J.R.R. Tolkien"},
    {"name": "George R.R. Martin"},
    {"name": "Agatha Christie"},
    {"name": "Mark Twain"},
]

# Add authors if they do not already exist
for author_data in authors_data:
    author, created = Author.objects.get_or_create(
        name=author_data["name"],
    )
    if created:
        print(f"Author '{author.name}' added.")
    else:
        print(f"Author '{author.name}' already exists.")



# List of books to add
books_data = [
    {"title": "1984", "publication_year": "1949", "author_name": "George Orwell"},
    {"title": "Animal Farm", "publication_year": "1945", "author_name": "George Orwell"},
    {"title": "Homage to Catalonia", "publication_year": "1938", "author_name": "George Orwell"},
    
    {"title": "To Kill a Mockingbird", "publication_year": "1960", "author_name": "Harper Lee"},
    {"title": "Go Set a Watchman", "publication_year": "2015", "author_name": "Harper Lee"},
    
    {"title": "Pride and Prejudice", "publication_year": "1813", "author_name": "Jane Austen"},
    {"title": "Sense and Sensibility", "publication_year": "1811", "author_name": "Jane Austen"},
    {"title": "Emma", "publication_year": "1815", "author_name": "Jane Austen"},
    
    {"title": "The Great Gatsby", "publication_year": "1925", "author_name": "F. Scott Fitzgerald"},
    {"title": "Tender is the Night", "publication_year": "1934", "author_name": "F. Scott Fitzgerald"},
    {"title": "This Side of Paradise", "publication_year": "1920", "author_name": "F. Scott Fitzgerald"},
    
    {"title": "Moby Dick", "publication_year": "1851", "author_name": "Herman Melville"},
    {"title": "Billy Budd, Sailor", "publication_year": "1924", "author_name": "Herman Melville"},
    
    {"title": "Harry Potter and the Philosopher's Stone", "publication_year": "1997", "author_name": "J.K. Rowling"},
    {"title": "Harry Potter and the Chamber of Secrets", "publication_year": "1998", "author_name": "J.K. Rowling"},
    
    {"title": "The Hobbit", "publication_year": "1937", "author_name": "J.R.R. Tolkien"},
    {"title": "The Lord of the Rings", "publication_year": "1954", "author_name": "J.R.R. Tolkien"},
    
    {"title": "A Game of Thrones", "publication_year": "1996", "author_name": "George R.R. Martin"},
    {"title": "A Clash of Kings", "publication_year": "1998", "author_name": "George R.R. Martin"},
    
    {"title": "Murder on the Orient Express", "publication_year": "1934", "author_name": "Agatha Christie"},
    {"title": "And Then There Were None", "publication_year": "1939", "author_name": "Agatha Christie"},
    
    {"title": "The Adventures of Tom Sawyer", "publication_year": "1876", "author_name": "Mark Twain"},
    {"title": "The Adventures of Huckleberry Finn", "publication_year": "1884", "author_name": "Mark Twain"},
]

# Add books if they do not already exist
for book_data in books_data:
    author = Author.objects.get(name=book_data["author_name"])
    book, created = Book.objects.get_or_create(
        title=book_data["title"],
        publication_year=book_data["publication_year"],
        author=author,
    )
    if created:
        print(f"Book '{book.title}' added.")
    else:
        print(f"Book '{book.title}' already exists.")


from django.contrib.auth.models import User

# Define dummy data for Users
users_data = [
    {"username": "john_smith", "email": "john@example.com", "password": "password123", "first_name": "John", "last_name": "Smith"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "password123", "first_name": "Jane", "last_name": "Smith"},
    {"username": "admin_user", "email": "admin@example.com", "password": "adminpassword", "first_name": "Admin", "last_name": "User"},
]

# Create Users
for user_data in users_data:
    user, created = User.objects.get_or_create(
        username=user_data["username"],
        defaults={
            "email": user_data["email"],
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
        }
    )
    if created:
        user.set_password(user_data["password"])
        user.save()

print("Database populated successfully!")

