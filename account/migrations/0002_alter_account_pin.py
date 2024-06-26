# Generated by Django 5.0.6 on 2024-06-26 11:09

import account.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pin',
            field=models.CharField(max_length=4, validators=[account.validator.validate_pin]),
        ),
    ]