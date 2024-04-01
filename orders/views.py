from django.shortcuts import render
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Order, OrderItem
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _


@login_required
def order_create_view(request):
    order_form = OrderForm(request.POST,)
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, _('You can\'t proceed to checkout page with empty cart.'))
        return redirect('product_list')
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.price
                )
            cart.clear()
            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()
            messages.success(request, _('Your order has been successfully placed.'))
    return render(request, 'orders/order_create.html', )
