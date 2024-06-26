# Generated by Django 5.0.6 on 2024-06-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
