["1984"]
retrieved_book = Book.objects.get(id=book.id)
retrieved_book
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
retrieved_book
