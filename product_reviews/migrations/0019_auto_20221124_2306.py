# Generated by Django 3.2 on 2022-11-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_reviews', '0018_auto_20221124_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created_on',
            field=models.DateTimeField(default='2022-11-24 23:06:40'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated_on',
            field=models.DateTimeField(default='2022-11-24 23:06:40'),
        ),
    ]
