from django.db import models
import locale

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

    user = models.ForeignKey(User, verbose_name="Comprador")
    products = models.ManyToManyField(Product, verbose_name="Produtos")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Data da venda")
    note = models.CharField(max_length=200, verbose_name="Observações")
    value = models.DecimalField(max_digits=16,decimal_places=2,verbose_name="Valor total")
    
    def __str__(self):
        return "Venda "+str(self.id)

    def listProductsString(self):
        productsString = ""
        for product in self.products.all():
            productsString += product.__str__()+", "
        return productsString[:-2]
    listProductsString.short_description = 'Lista de produtos'
