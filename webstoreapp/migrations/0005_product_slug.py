# Generated by Django 3.2.12 on 2022-02-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstoreapp', '0004_alter_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='asd', verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
