from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), verbose_name=_('User'), on_delete=models.CASCADE)
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    phone_number = models.CharField(_('Phone Number'), max_length=15)
    address = models.CharField(_('Address'), max_length=700)
    is_paid = models.BooleanField(_('Is paid?'), default=False)
    datetime_created = models.DateTimeField(_('Time Created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Time modified'), auto_now=True)
    order_notes = models.CharField(_('Order Note'), max_length=700, blank=True)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1, )
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"Order item {self.id}: {self.product.title} X {self.quantity} price:{self.price}"
