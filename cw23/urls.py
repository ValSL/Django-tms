from django.urls import path
from .views import api_products, api_product_detail

urlpatterns = [
    path('product/', api_products),
    path('product/<int:pk>', api_product_detail),
]