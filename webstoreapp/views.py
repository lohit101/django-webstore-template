from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products_all = Product.objects.all()
    products = Product.objects.all()[:8]
    grid = 8
    context = {
        'products' : products,
        'products_all' : products_all,
    }
    return render(request, 'home.html', context)

def products(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'products.html', context)