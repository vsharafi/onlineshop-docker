from django.contrib import admin
from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ('text', 'author', 'active', 'stars', 'id')
    extra = 0
    # max_num = 10


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'datetime_created', 'datetime_modified', 'active', 'id')
    inlines = [CommentsInline, ]

@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'text', 'author', 'datetime_created', 'datetime_modified', 'active', 'stars', 'id')
    list_filter = ('author', 'datetime_created', 'datetime_modified')