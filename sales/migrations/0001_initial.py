# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations

def initial_data_users(apps,schema_editor):
    User = apps.get_model("sales",User)
    User(name="Usuário 1").save()
    User(name="Usuário 2").save()
    User(name="Usuário 3").save()
    User(name="Usuário 4").save()
    User(name="Usuário 5").save()
    User(name="Usuário 6").save()

def initial_data_products(apps,schema_editor):  
    Product = apps.get_model("sales",Product)
    Product(price=11.30,name="Produto 1").save()
    Product(price=21.30,name="Produto 2").save()
    Product(price=14.30,name="Produto 3").save()
    Product(price=12.50,name="Produto 4").save()
    Product(price=14.50,name="Produto 5").save()
    Product(price=21.40,name="Produto 6").save()
    Product(price=41.20,name="Produto 7").save()
    Product(price=21.40,name="Produto 8").save()
    Product(price=31.30,name="Produto 9").save()
    Product(price=14.40,name="Produto 10").save()
    Product(price=21.32,name="Produto 11").save()
    Product(price=13.21,name="Produto 12").save()
    Product(price=14.31,name="Produto 13").save()
    Product(price=14441,name="Produto 14").save()
    Product(price=2213123,name="Produto 15").save()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('price', models.DecimalField(max_digits=16, decimal_places=2)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(to_field='id', to='sales.User')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(max_length=200)),
                ('value', models.DecimalField(max_digits=16, decimal_places=2)),
                ('products', models.ManyToManyField(to='sales.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RunPython(initial_data_users),
        migrations.RunPython(initial_data_products)
    ]
