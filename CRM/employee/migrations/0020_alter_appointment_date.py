# Generated by Django 4.2.3 on 2023-07-20 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_alter_doctor_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
