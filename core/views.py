from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'backend/dashboard.html')



def products(request):
    return render(request, 'backend/products.html')


def create_product(request):
    return render(request, 'backend/create-product.html')


def categories(request):
    return render(request, 'backend/categories.html')


def orders(request):
    return render(request, 'backend/orders.html')


def order_detail(request):
    return render(request, 'backend/order-detail.html')


def users(request):
    return render(request, 'backend/users.html')


def user_detail(request):
    return render(request, 'backend/user-detail.html')


def user_detail_wishlist(request):
    return render(request, 'backend/user-detail-wishlist.html')

def user_detail_cart(request):
    return render(request, 'backend/user-detail-cart.html')

def user_detail_address(request):
    return render(request, 'backend/user-detail-address.html')

def messages(request):
    return render(request, 'backend/messages.html')

def notifications(request):
    return render(request, 'backend/notifications.html')

def payments(request):
    return render(request, 'backend/payments.html')

def create_voucher(request):
    return render(request, 'backend/create-voucher.html')

def vouchers(request):
    return render(request, 'backend/vouchers.html')

def profile(request):
    return render(request, 'backend/profile.html')

def profile_payments(request):
    return render(request, 'backend/profile-payments.html')

def login(request):
    return render(request, 'backend/login.html')
