# Generated by Django 4.2.3 on 2023-07-17 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0013_alter_doctor_entered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealsdetail',
            name='entered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]
