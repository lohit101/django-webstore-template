from django.shortcuts import render, HttpResponse, redirect
from django.template import RequestContext
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
    if request.method == 'POST':
        if 'product' in request.COOKIES.keys():
            addToCart = request.POST.get('addToCart')
            response = redirect('productView', slug=addToCart)
            response.set_cookie('product', str(request.COOKIES['product']) + ';' + str(addToCart))
            print(request.COOKIES['product'])
            return response
        else:
            addToCart = request.POST.get('addToCart')
            response = redirect('productView', slug=addToCart)
            response.set_cookie('product', addToCart)
            return response

    else:
        product = Product.objects.get(slug=slug)
        products_suggestion = Product.objects.all().filter(featured=True)
        if 'product' in request.COOKIES.keys() and str(slug) in request.COOKIES['product']:
            context = {
                'product' : product,
                'products_suggestion' : products_suggestion,
                'cookie' : request.COOKIES['product'],
            }
        else:
            context = {
            'product' : product,
            'products_suggestion' : products_suggestion,
        }
    return render(request, 'productview.html', context)

def cart(request):
    if request.method == 'POST':
        remove = request.POST.get('remove')
        if str(';' + str(remove)) in request.COOKIES['product']:
            intel = str(request.COOKIES['product'])
            new_cookie = intel.replace(str(';' + str(remove)), '')
            response = redirect('cart')
            response.set_cookie('product', new_cookie)
            return response
        elif str(str(remove) + ';') in request.COOKIES['product']:
            intel = str(request.COOKIES['product'])
            new_cookie = intel.replace(str(str(remove) + ';'), '')
            response = redirect('cart')
            response.set_cookie('product', new_cookie)
            return response
        elif str(remove) == request.COOKIES['product']:
            response = redirect('cart')
            response.delete_cookie('product')
            return response

    else:
        if 'product' in request.COOKIES.keys():
            if ';' in request.COOKIES['product']:
                items = request.COOKIES['product'].split(';')
                products = Product.objects.filter(slug__in=items)
            else:
                items = request.COOKIES['product']
                products = Product.objects.filter(slug=items)
            context = {
                'products' : products,
            }
            return render(request, 'cart.html', context)
        else:
            context = {
                'cartInfo' : True,
            }
            return render(request, 'cart.html', context)