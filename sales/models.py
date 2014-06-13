from django.db import models

# Create your models here.
class Product(models.Model):
    price = models.DecimalField(max_digits=16,decimal_places=2)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sale(models.Model):
    user = models.ForeignKey(User)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=16,decimal_places=2)

    def __str__(self):
        return self.id