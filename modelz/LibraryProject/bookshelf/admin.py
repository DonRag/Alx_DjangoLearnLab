from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("title", "author", "publication_year")
    
    # Filters in the admin interface
    list_filter = ("author",)
    
    # Search functionality in the admin interface
    search_fields = ("title", "author")
