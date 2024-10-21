from django.urls import path
from .views import*

urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('checkout/', checkout, name="checkout"),
    path('wishlist/', wishlist, name="wishlist"),
    path('left_sidebar/', left_sidebar, name="shop-left-sidebar"),
    path('product-left-sidebar/', product_left_sidebar, name="product-left-sidebar"),
    path('about/', about, name="about"),
    path('Contact/', Contact, name="contact-us"),
    path('cart/', cart, name="cart"),
    path('track_order/', track_order, name="track-order"),
    path('FAQ/', FAQ, name="faq"),
    path('policy/', policy, name="policy"),
    path('blog_sidebar/', blog_sidebar, name="blog-left-sidebar"),
    path('blog_detail_lef_sidebar/', blog_detail_left_sidebar, name="blog-detail-left-sidebar"),
    path('elements_product/', elements_product, name="elements-products"),
    path('terms/', terms, name="terms"),
    path('forgot/', forgot, name="forgot"),
]