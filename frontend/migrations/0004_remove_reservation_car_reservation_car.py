# Generated by Django 5.0.2 on 2024-03-17 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_alter_car_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='car',
        ),
        migrations.AddField(
            model_name='reservation',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='frontend.car'),
        ),
    ]
