# Generated by Django 3.2 on 2022-11-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20221123_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default='2022-11-24 12:09:10'),
        ),
    ]