# Generated by Django 2.1.14 on 2020-06-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default='null', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.FloatField(max_length=100),
        ),
    ]
