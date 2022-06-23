from django.db import models

# Create your models here.
class Book(models.Model):
    Book = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published = models.CharField(max_length=25)

    def __str__(self):
        return self.Book