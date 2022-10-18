from django.shortcuts import render
from books.models import Book


def main_page(request):
    template = 'books/main_page.html'
    return render(request, template)


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().values()
    context = {'books': books}
    return render(request, template, context)


def books_by_date(request, slug):
    books = Book.objects.filter(pub_date=slug)
    books_next = Book.objects.filter(pub_date__gt=slug).values().first()
    books_previous = Book.objects.filter(pub_date__lt=slug).values().first()
    template = 'books/books_by_date.html'
    context = {'books': books,
               'previous': books_previous,
               'next': books_next,
               'url': '/books/'
              }
    return render(request, template, context)

