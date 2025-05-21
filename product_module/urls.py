from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
]