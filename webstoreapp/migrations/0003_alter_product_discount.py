# Generated by Django 3.2.12 on 2022-02-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstoreapp', '0002_alter_product_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=0, max_length=5, verbose_name='Discounted Price (INR)'),
        ),
    ]
