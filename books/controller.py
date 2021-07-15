from django.shortcuts import render
from .models import Book


def list(requests):
    '''Obtener todos los libros'''

    book_list = Book.get_all_books()  # acceso a los datos

    return render(requests, 'list.html', locals())  # definición de la vista (template) a mostrar


def book(requests, pk):
    '''Obtener la información del libro con pk definido'''

    book_obj = Book.get_book(pk=pk)  # acceso a los datos

    return render(requests, 'book.html', locals())  # definición de la vista (template) a mostrar
