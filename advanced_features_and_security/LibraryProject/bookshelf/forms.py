from django import forms
from .models import Book

# ExampleForm for creating or updating a Book
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'author']
        
    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Perform any necessary validation or cleaning
        if not title:
            raise forms.ValidationError("Title is required")
        return title

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        # Perform validation or cleaning
        if len(isbn) != 13:
            raise forms.ValidationError("ISBN must be 13 characters long")
        return isbn
