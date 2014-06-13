from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sales.models import User
from sales.models import Product
from sales.models import Sale

admin.site.register(Sale)