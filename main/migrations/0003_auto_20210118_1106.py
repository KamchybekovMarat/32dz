# Generated by Django 3.1.3 on 2021-01-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bookstore'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookstore',
            options={'verbose_name': 'Книжный магазин', 'verbose_name_plural': 'Книжные магазины'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
