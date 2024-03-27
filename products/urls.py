from django.urls import path
from .views import ProductListView, ProductDetailView, CommentCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    # path('<int:pk>/', product_detail, name='product_detail'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]
