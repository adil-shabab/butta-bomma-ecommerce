from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'), 
    path('products', products, name='products'), 
    path('create/product', create_product, name='create_product'), 
    path('categories', categories, name='categories'), 
    path('orders', orders, name='orders'), 
    path('orders/detail', order_detail, name='order_detail'), 
    path('messages', messages, name='messages'), 
    path('users', users, name='users'), 
    path('users/detail', user_detail, name='user_detail'), 
    path('users/detail/address', user_detail_address, name='user_detail_address'), 
    path('users/detail/cart', user_detail_cart, name='user_detail_cart'), 
    path('users/detail/wishlist', user_detail_wishlist, name='user_detail_wishlist'), 
]