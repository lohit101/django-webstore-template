from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def home(request):
    products_featured = Product.objects.all().order_by('-in_stock').filter(featured=True)
    products = Product.objects.all().order_by('-in_stock')[:8]
    context = {
        'products' : products,
        'products_featured' : products_featured,
    }
    return render(request, 'home.html', context)

def products(request):
    products = Product.objects.all().order_by('-in_stock')
    context = {
        'products' : products,
    }
    return render(request, 'products.html', context)

def search(request):
    search_query = request.POST.get('searchInput')
    products = Product.objects.all().order_by('-in_stock').filter(product_name__contains=search_query)
    context = {
        'products' : products,
        'search_query' : search_query,
    }
    return render(request, 'search.html', context)

def productView(request, slug):
    product = Product.objects.get(slug=slug)
    products_suggestion = Product.objects.all().filter(featured=True)
    context = {
        'product' : product,
        'products_suggestion' : products_suggestion,
    }
    return render(request, 'productview.html', context)

def checkout(request):
    return render(request, 'checkout.html')