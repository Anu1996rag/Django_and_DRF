# Generated by Django 2.2 on 2021-04-24 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_mngt', '0006_auto_20210424_1243'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StockHistory',
        ),
    ]