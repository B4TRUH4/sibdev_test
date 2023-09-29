# Generated by Django 4.2.5 on 2023-09-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=100, verbose_name='покупатель')),
                ('item', models.CharField(max_length=100, verbose_name='товар')),
                ('total', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='сумма')),
                ('quantity', models.PositiveIntegerField(verbose_name='количество')),
                ('date', models.DateTimeField(verbose_name='дата и время')),
            ],
            options={
                'verbose_name': ('Сделка',),
                'verbose_name_plural': ('Сделки',),
            },
        ),
    ]