# Generated by Django 5.0.2 on 2024-03-14 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='availability',
            field=models.BooleanField(),
        ),
    ]
