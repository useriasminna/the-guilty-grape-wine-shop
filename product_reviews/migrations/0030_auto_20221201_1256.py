# Generated by Django 3.2 on 2022-12-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_reviews', '0029_auto_20221129_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_created_on',
            field=models.DateTimeField(default='2022-12-01 12:56:10'),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_updated_on',
            field=models.DateTimeField(default='2022-12-01 12:56:10'),
        ),
    ]
