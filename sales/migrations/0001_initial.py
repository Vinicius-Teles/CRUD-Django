# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('user', models.ForeignKey(to='sales.User', verbose_name='Comprador', to_field='id')),
                ('date', models.DateTimeField(verbose_name='Data da venda', auto_now_add=True)),
                ('note', models.TextField(max_length=200, verbose_name='Observações')),
                ('trace_code', models.CharField(max_length=13, verbose_name='Código de rastreamento')),
                ('value', models.DecimalField(verbose_name='Valor total', decimal_places=2, max_digits=16)),
                ('products', models.ManyToManyField(to='sales.Product', verbose_name='Produtos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
