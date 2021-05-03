# Generated by Django 2.2 on 2021-04-20 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_mngt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Computer Peripherals', 'Computer Peripherals'), ('Stationary', 'Stationary')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
