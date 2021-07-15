from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=300)
    writer = models.CharField(max_length=300)
