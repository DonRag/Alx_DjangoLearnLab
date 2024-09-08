# Django Shell CRUD Operations with the Book Model

This document outlines the process of performing CRUD (Create, Read, Update, Delete) operations on the `Book` model using Django's ORM through the Django shell.

---

## 1. Setting Up the Django Shell

```bash
$ python manage.py shell
```

This command launches the Django interactive shell, allowing us to interact with the database using Python commands.

---

## 2. Importing the Book Model

```python
>>> from bookshelf.models import Book
```

Before performing any CRUD operations, we need to import the `Book` model from our `bookshelf` app.

---

## 3. Creating a New Book Record

### Command:

```python
>>> # Creating a new book
>>> new_book = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
... )
```

### Explanation:

- **`Book.objects.create()`**: This method is used to create a new record in the `Book` table.
- **Parameters**:
  - `title="1984"`: The title of the book.
  - `author="George Orwell"`: The author of the book.
  - `publication_year=1949`: The year the book was published.

### Verifying the Creation:

```python
>>> all_books = Book.objects.all()
>>> for book in all_books:
...     print(book.title, book.author, book.publication_year)
...
1984 George Orwell 1949
```

- **`Book.objects.all()`**: Retrieves all the records in the `Book` table.
- **`for book in all_books:`**: Iterates through the queryset to print out the details of each book.

---

## 4. Retrieving All Book Records

### Command:

```python
>>> from bookshelf.models import Book
>>> # Retrieve command
>>> all_books = Book.objects.all()
>>> for book in all_books:
...     print(book.title, book.author, book.publication_year)
...
```

### Explanation:

- This command sequence retrieves all book records stored in the database and prints each book's title, author, and publication year.

### Output:

```python
1984 George Orwell 1949
```

---

## 5. Updating an Existing Book Record

### Command:

```python
>>> # Updating the title of the book
>>> book = Book.objects.get(title="1984")
>>> # Update Command
>>> book.title = "Nineteen Eighty-Four"
>>> book.save() # Saving the changes to the database
```

### Explanation:

- **`Book.objects.get(title="1984")`**: Fetches the specific book record where the title is "1984".
- **Updating**: The `title` field is updated to "Nineteen Eighty-Four".
- **Saving**: The `book.save()` method persists the changes to the database.

### Verifying the Update:

```python
>>> books = Book.objects.all()
>>> for book in books:
...     print(book.title, book.author, book.publication_year)
...
Nineteen Eighty-Four George Orwell 1949
```

- This verifies that the book title was successfully updated.

---

## 6. Deleting a Book Record

### Command:

```python
>>> # Deleting a record
>>> # Fetching the book record
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> # Delete Command
>>> book.delete()
(1, {'bookshelf.Book': 1})
```

### Explanation:

- **Fetching**: The specific book record is fetched using `Book.objects.get(title="Nineteen Eighty-Four")`.
- **Deleting**: The `book.delete()` command deletes the fetched record from the database.
- **Output**: `(1, {'bookshelf.Book': 1})` indicates that one record was successfully deleted.

---

## Conclusion

This document demonstrates how to perform basic CRUD operations using Django's ORM through the Django shell. Each operation, Create, Read, Update, Delete, was executed with appropriate comments explaining the commands used and the expected outcomes.
