from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        user = request.user
        if form.is_valid():
            form.save()
            # save user_name
            if 'first_name' in request.POST:
                user.first_name = request.POST['first_name']
                user.save()
            if 'last_name' in request.POST:
                user.last_name = request.POST['last_name']
                user.save()
            messages.success(request, 'profile updated successfully')
        else:
            messages.error(request, 'update failed. please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'this is a past confirmation for order number {order_number}. '
        'a confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
