# Generated by Django 4.1.5 on 2023-01-04 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='name',
            field=models.CharField(default='Jordan Shoe', max_length=50),
            preserve_default=False,
        ),
    ]
