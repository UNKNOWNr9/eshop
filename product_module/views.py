from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.
class ProductList(ListView):
    template_name = 'product_module/product_list.html'
    queryset = Product.objects.filter(is_active=True)
    context_object_name = 'products'

class ProductDetail(DetailView):
    template_name = 'product_module/product_detail.html'
    queryset = Product.objects.filter(is_active=True)
    context_object_name = 'products'