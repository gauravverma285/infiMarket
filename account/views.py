from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def checkout(request):
    return render(request, 'checkout.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def left_sidebar(request):
    return render(request, 'shop-left-sidebar.html')

def product_left_sidebar(request):
    return render(request, 'product-left-sidebar.html')

def about(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request , 'contact-us.html')

def cart(request):
    return render(request , 'cart.html')

def track_order(request):
    return render(request , 'track-order.html')

def FAQ(request):
    return render(request , 'faq.html')

def policy(request):
    return render(request , 'policy.html')

def blog_sidebar(request):
    return render(request , 'blog-left-sidebar.html')

def elements_product(request):
    return render(request , 'elements-products.html')

def terms(request):
    return render(request , 'terms.html')

def forgot(request):
    return render(request , 'forgot.html')