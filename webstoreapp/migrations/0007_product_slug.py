# Generated by Django 3.2.12 on 2022-02-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstoreapp', '0006_auto_20220215_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=64, verbose_name='Slug'),
        ),
    ]