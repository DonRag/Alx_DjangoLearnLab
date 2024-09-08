from api.models import Book
from django.contrib.auth.models import User

# Fetch all books
books = Book.objects.all()

# Fetch the admin user
admin_user = User.objects.get(username='admin_user')

# Fetch other users (excluding admin)
users = User.objects.filter(username__in=['john_smith', 'jane_smith'])

# Initialize a counter to alternate between non-admin users
user_count = len(users)
counter = 0

# Update the owner field for each book
for book in books:
    if not book.owner:  # Only assign if no owner is set
        # Assign the book to a user in a round-robin manner
        book.owner = users[counter % user_count]
        book.save()
        print(f"Book '{book.title}' updated with owner '{book.owner.username}'.")

# Ensure all books are also owned by the admin
for book in books:
    book.owner = admin_user
    book.save()
    print(f"Book '{book.title}' updated with owner 'admin_user'.")

print("Books updated successfully with round-robin ownership and admin access.")
