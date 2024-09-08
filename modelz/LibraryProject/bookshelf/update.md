# Updating an Existing Book Record
``` python
Python 3.12.4 (main, Jun  6 2024, 18:26:44) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> # updating the title of the book
>>> book.title = "Nineteen Eighty-Four"
>>> book.save() # Saving the changes to the database
>>> # Retrieving all the books to verify update
>>> all_books = Book.objects.all()
>>> for book in all_books:
...     print(book.title, book.author, book.publication_year)
... 
Nineteen Eighty-Four George Orwell 1949
```
### Explanation:
- **`Book.objects.get(title="1984")`**: Fetches the specific book record where the title is "1984".
- **Updating**: The `title` field is updated to "Nineteen Eighty-Four".
- **Saving**: The `book.save()` method persists the changes to the database.