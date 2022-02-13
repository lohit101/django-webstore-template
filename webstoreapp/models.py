from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(
        max_length=50,
        verbose_name='Product Name *',
        blank=False
    )
    product_details = models.CharField(
        max_length=500,
        verbose_name='Product Details *',
        blank=False
    )
    price = models.CharField(
        max_length=10,
        verbose_name='Price (INR) *',
        blank=False
    )
    discount = models.CharField(
        max_length=10,
        verbose_name='Discounted Price (INR)',
        blank=True
    )
    product_image = models.CharField(
        max_length=100,
        verbose_name='Product Image *',
        blank=False
    )
    featured = models.BooleanField(
        verbose_name='Featured',
        default=''
    )
    stock_out = models.BooleanField(
        verbose_name='Out of Stock',
        default=''
    )
    #add another field for foot size

    def __str__(self):
        return self.product_name