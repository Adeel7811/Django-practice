from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50, null=True, blank=True)
    publuish_date = models.DateField
    price = models.CharField(max_length=50, null=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=2000)

