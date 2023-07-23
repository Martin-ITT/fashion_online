from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    grand_total = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total = quantity * product.price
        grand_total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'price': product.price,
            'quantity': quantity,
            'product':product,
            'total': total,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context