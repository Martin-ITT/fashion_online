from django.shortcuts import render

# Create your views here.

# bag content page
def view_bag(request):
    
    return render(request, 'bag/bag.html')