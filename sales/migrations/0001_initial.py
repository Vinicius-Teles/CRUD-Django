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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=16, decimal_places=2)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(verbose_name='Comprador', to_field='id', to='sales.User')),
                ('date', models.DateTimeField(verbose_name='Data da venda', auto_now_add=True)),
                ('note', models.CharField(verbose_name='Observações', max_length=200)),
                ('value', models.DecimalField(verbose_name='Valor total', decimal_places=2, max_digits=16)),
                ('products', models.ManyToManyField(to='sales.Product', verbose_name='Produtos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
