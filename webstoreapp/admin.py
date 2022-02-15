from django.contrib import admin
from webstoreapp.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'in_stock')
    readonly_fields = ['slug']

# Register your models here.
admin.site.register(Product, ProductAdmin)
