# Generated by Django 3.2 on 2022-11-21 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_reviews', '0009_auto_20221119_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created_on',
            field=models.DateTimeField(default='2022-11-21 11:21:25'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated_on',
            field=models.DateTimeField(default='2022-11-21 11:21:25'),
        ),
    ]
