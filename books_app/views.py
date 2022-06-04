from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView


# Create your views here.
from django.views import View

from books_app.forms import AddAuthorForm, AddBookForm
from books_app.models import Author


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class ShowNumberView(View):
    def get(self, request, n):
        numbers = list(range(n))
        return render(request, 'base.html', {'numbers': numbers})


class AddAuthorView(View):

    def get(self, request):
        form = AddAuthorForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})




class AddBookView(PermissionRequiredMixin, View):

    permission_required = ['books_app.add_book']

    def get(self, request):
        form = AddBookForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})


class AuthorList(View):

    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'list_view.html', {'authors':authors})

