# Creating a New Book Record
```python
Python 3.12.4 (main, Jun  6 2024, 18:26:44) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> new_book = Book.objects.create(
... title="1984",
... author="George Orwell",
... publication_year=1949
... )
>>> all_books = Book.objects.all()
>>> for book in all_books:
...     print(book.title, book.author, book.publication_year)
... 
1984 George Orwell 1949
>>> 
>>> 
>>> 
```
### Explanation:
- **`Book.objects.create()`**: This method is used to create a new record in the `Book` table.
- **Parameters**:
  - `title="1984"`: The title of the book.
  - `author="George Orwell"`: The author of the book.
  - `publication_year=1949`: The year the book was published.
- **`Book.objects.all()`**: Retrieves all the records in the `Book` table.
- **`for book in all_books:`**: Iterates through the queryset to print out the details of each book.