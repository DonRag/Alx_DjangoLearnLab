# Importing all the necessary models
from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books written by a specific author (e.g., George Orwell)
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

print(f"Books by {author_name}:")
for book in books_by_author:
    print(f"- {book.title}")

# Query 2: List all books in a specific library (e.g., Chiron Library)
library_name = "Chiron Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

print(f"\nBooks in {library_name}:")
for book in books_in_library:
    print(f"- {book.title} by {book.author.name}")

# Query 3: Retrieve the librarian for a specific library (e.g., Chiron Library)
librarian_of_library = Librarian.objects.get(library=library)

print(f"\nLibrarian of {library_name}:")
print(f"- {librarian_of_library.name}")

# Query 4: List all libraries that have a specific book (e.g., "1984")
book_title = "1984"
book = Book.objects.get(title=book_title)
libraries_with_book = Library.objects.filter(books=book)

print(f"\nLibraries that have the book '{book_title}':")
for lib in libraries_with_book:
    print(f"- {lib.name}")

# Query 5: List all books across all libraries
all_books = Book.objects.all()

print("\nAll books in the system:")
for book in all_books:
    print(f"- {book.title} by {book.author.name}")
