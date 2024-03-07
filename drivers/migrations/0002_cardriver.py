# Generated by Django 5.0.2 on 2024-02-27 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
        ('employees', '0004_alter_car_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.car')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver', verbose_name='Driver')),
            ],
        ),
    ]