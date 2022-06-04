from django import forms

from books_app.models import Author, Book


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'