from django.db import models

from django.db.models.signals import pre_save
import string
import random

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(
        max_length=50,
        verbose_name='Product Name *',
        blank=False
    )
    product_details = models.CharField(
        max_length=499,
        verbose_name='Product Details *',
        blank=False
    )
    price = models.IntegerField(
        max_length=5,
        verbose_name='Price (INR) *',
        blank=False,
        null=False,
        default=0
    )
    discount = models.IntegerField(
        max_length=5,
        verbose_name='Discounted Price (INR)',
        blank=True,
        null=True,
    )
    product_image = models.ImageField(
        upload_to='media/',
        verbose_name='Product Image *',
        blank=False
    )
    featured = models.BooleanField(
        verbose_name='Featured',
        default=''
    )
    in_stock = models.BooleanField(
        verbose_name='In Stock',
        default=True
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=64,
        default=''.join(random.choices(string.ascii_letters + string.digits, k = 32)),
        blank=False
    )
    #add another field for foot size

    class Meta:
        ordering = ('-in_stock',)

    def __str__(self):
        return self.product_name