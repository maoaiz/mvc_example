from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=300)
    writer = models.CharField(max_length=300)

    @staticmethod
    def get_all_books():
        return Book.objects.all()

    @staticmethod
    def get_book(pk):
        return Book.objects.get(pk=pk)
