from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

# all products page, inc sort & search
def all_products(request):

    products = Product.objects.all()
    query = None
    
    # search funcionality
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any criteria!")
                return redirect(reverse('products'))
            
            # handling search funcionality for both product name and description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

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