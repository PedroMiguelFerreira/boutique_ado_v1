from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LosuqEJvgjDC8ytqp2jUB4lUQMCKweQ5B7sM7ZA3UatT0GAkvr0h1mzEO3noWxJT8vrbzFoNT166td96sx2r3WH00UU0i6EZq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
