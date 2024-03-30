from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/product_cover', blank=True, verbose_name=_('Product Image'))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [('1', _('Very bad')), ('2', _('Bad')), ('3', _('Normal')), ('4', _('Good')), ('5', _('Very good'))]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name=_('Comment Text'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    active = models.BooleanField(default=True)
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, default=PRODUCT_STARS[2],
                             verbose_name=_("product stars"))

    objects = models.Manager()
    active_comments = ActiveCommentManager()
    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
