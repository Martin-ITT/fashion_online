from decimal import Decimal

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    grand_total = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count' product_count,
        'grand_total': grand_total,
    }

    return context