# Generated by Django 3.2 on 2022-11-18 21:08

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20221109_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
