# Generated by Django 4.2.5 on 2023-09-28 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_customer_gem_alter_deal_options_alter_deal_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)], verbose_name='сумма'),
        ),
    ]
