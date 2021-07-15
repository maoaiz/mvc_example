from django.shortcuts import render
from .models import Book


def list(requests):
    '''Obtener todos los libros'''

    book_list = Book.objects.all()
    return render(requests, 'list.html', locals())


def book(requests, pk):
    '''Obtener la información del libro con pk definido'''

    book_obj = Book.objects.get(pk=pk)
    return render(requests, 'book.html', locals())
