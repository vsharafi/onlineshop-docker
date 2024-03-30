from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .cart import Cart
from .forms import AddProductToCartForm
from django.views.decorators.http import require_POST


def cart_detail_view(request):
    cart = Cart(request)
    total = 0
    for item in cart:
        item['product_quantity_update_form'] = AddProductToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddProductToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        replace_current_quantity = cleaned_data['inplace']
        cart.add(product, quantity, replace_current_quantity)
    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
