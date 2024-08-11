from bookshelf.models import Book

# Create a new book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
retrieved_book = Book.objects.get(id=book.id)
retrieved_book
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book
retrieved_book.delete()

# Confirm the deletion
Book.objects.all()
