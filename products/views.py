from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Comment
from .forms import CommentForm
from django.shortcuts import reverse, get_object_or_404, redirect, render
from django.contrib import messages
from django.utils.translation import gettext as _


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(active=True).order_by('-datetime_modified')
    paginate_by = 1

    # def get_queryset(self):
    #     return Product.objects.filter(active=True).order_by('-datetime_modified')


# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.product = product
#             new_comment.author = request.user
#             new_comment.save()
#             return redirect('product_detail', pk=pk)
#     return render(request, 'products/product_detail.html', {'product': product, 'form': form})
#

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        # context['add_to_cart_form'] = AddProductToCartForm()
        return context

    # def post(self, request, *args, **kwargs):
    #     form = CommentForm()
    #     form = CommentForm(request.POST)
    #     obj = form.save(commit=False)
    #     obj.product = get_object_or_404(Product, pk=self.kwargs['pk'])
    #     obj.author = request.user
    #     obj.save()
    #     form = CommentForm()
    #     return render(request, 'products/product_detail.html', {'form': form, 'product': obj.product})


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'products/product_detail.html'
    context_object_name = 'form'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        new_comment = form.save(commit=False)
        new_comment.author = self.request.user
        new_comment.product = product
        messages.success(self.request, _('Your comment was successfully submitted'))
        return super().form_valid(form)
