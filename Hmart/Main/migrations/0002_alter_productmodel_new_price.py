# Generated by Django 4.1.3 on 2022-11-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='new_price',
            field=models.FloatField(verbose_name='Новая цена'),
        ),
    ]
