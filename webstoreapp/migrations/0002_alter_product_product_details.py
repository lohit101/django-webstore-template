# Generated by Django 3.2.12 on 2022-02-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_details',
            field=models.CharField(max_length=499, verbose_name='Product Details *'),
        ),
    ]
