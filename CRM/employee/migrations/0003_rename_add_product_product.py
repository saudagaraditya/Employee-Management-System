# Generated by Django 4.2.3 on 2023-07-16 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_add_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_Product',
            new_name='Product',
        ),
    ]
