from django.shortcuts import render
from .models import Product

# Create your views here.

# all products page, inc sort & search
def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)