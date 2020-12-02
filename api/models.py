from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Medecines(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    number = models.PositiveIntegerField()
    description = models.CharField(max_length=20)
    items = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.number},{self.description}'


class Stock(models.Model):
    products = models.CharField(max_length=50)
    description = models.TextField(max_length=30)

    def __str__(self):
        return f'{self.products},{self.description}'


class Sells(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=20)
