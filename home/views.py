from django.shortcuts import render
from products.models import Product # test

# Create your views here.

# home page
def index(request):
    
    products = Product.objects.all() # test
    print(products) # test

    return render(request, 'home/index.html')