from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(active=True).order_by('-datetime_modified')
    paginate_by = 1

    # def get_queryset(self):
    #     return Product.objects.filter(active=True).order_by('-datetime_modified')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
