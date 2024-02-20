# Generated by Django 4.2.3 on 2023-07-17 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealsDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.IntegerField()),
                ('entered_by', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.doctor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.product')),
            ],
        ),
    ]
