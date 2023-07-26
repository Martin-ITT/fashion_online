from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    id_selector = ""
    total = 0
    product_count = 0
    grand_total = 0
    bag = request.session.get('bag', {})

    # product has no sizes
    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total = item_data * product.price
            grand_total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id, #product id
                'price': product.price, #price
                'quantity': item_data, #quantity
                'product':product, #product
                'total': total, #qty*price
                'id_selector': item_id, #product id
            })
        # product has many sizes
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                # id selector will hold product id along with size
                # this if for correct rendering ang jquery element lookup
                id_selector = "id_" + str(item_id) + "_size_" + str(size)
                total = quantity * product.price
                product_count += quantity
                grand_total += quantity * product.price
                bag_items.append({
                    'item_id': item_id,
                    'price': product.price,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'total': total,
                    'id_selector': id_selector,

                })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'id_selector': id_selector,
    }

    return context