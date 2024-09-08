from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Author, Book
from django.contrib import messages
from .forms import ExampleForm

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('profile')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'bookshelf/login.html')

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')

# Profile view
@login_required
def profile(request):
    return render(request, 'bookshelf/profile.html', {'user': request.user})


# View to list all books (requires view permission)
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

# View to add a new book (requires create permission)
@login_required
@permission_required('bookshelf.can_create_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        isbn = request.POST.get('isbn')
        author_id = request.POST.get('author_id')
        # Assuming you have the author object already fetched
        author = get_object_or_404(Author, id=author_id)
        book = Book.objects.create(title=title, isbn=isbn, author=author)
        messages.success(request, "Book added successfully.")
        return redirect('book_list')
    return render(request, 'bookshelf/add_book.html')

# View to edit a book (requires edit permission)
@login_required
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.isbn = request.POST.get('isbn')
        book.author_id = request.POST.get('author_id')
        book.save()
        messages.success(request, "Book updated successfully.")
        return redirect('book_list')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# View to delete a book (requires delete permission)
@login_required
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})    
    

# View to demonstrate form handling and validation
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the book to the database
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
