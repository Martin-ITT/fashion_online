from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

# all products page, inc sort & search
def all_products(request):

    products = Product.objects.all()
    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


# detailed product page
def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)