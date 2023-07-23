from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.

# all products page, inc sort & search
def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    
    # search, sorting funcionality and category selection
    if request.GET:

        # sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # categories
        if 'category' in request.GET:
            category = request.GET['category']
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # search
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any criteria!")
                return redirect(reverse('products'))
            
            # handling search funcionality for both product name and description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,

    }
    
    return render(request, 'products/products.html', context)


# detailed product page
def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)