# Generated by Django 4.2.3 on 2023-07-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0018_alter_product_entered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
