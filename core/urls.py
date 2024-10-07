from django.urls import path
from .views import *


urlpatterns = [
    path('account/', dashboard, name='dashboard'), 
    path('account/signup/', signup, name='signup'),
    path('account/login/', login_view, name='login'),
    # path('account/logout/', logout_view, name='logout'),    
    path('account/notifications', notifications, name='notifications'), 
    path('account/payments', payments, name='payments'), 
    path('account/products', products, name='products'), 
    path('account/create/product', create_product, name='create_product'), 
    path('account/categories', categories, name='categories'), 
    path('account/orders', orders, name='orders'), 
    path('account/orders/detail', order_detail, name='order_detail'), 
    path('account/messages', messages, name='messages'), 
    path('account/vouchers', vouchers, name='vouchers'), 
    path('account/vouchers/create', create_voucher, name='create_voucher'), 
    path('account/profile', profile, name='profile'), 
    path('account/profile/payments', profile_payments, name='profile_payments'), 
    path('account/users', users, name='users'), 
    path('account/users/detail', user_detail, name='user_detail'), 
    path('account/users/detail/address', user_detail_address, name='user_detail_address'), 
    path('account/users/detail/cart', user_detail_cart, name='user_detail_cart'), 
    path('account/users/detail/wishlist', user_detail_wishlist, name='user_detail_wishlist'), 
]