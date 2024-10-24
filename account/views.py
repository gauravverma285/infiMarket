from django.shortcuts import render
from .models import User_Registration
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    return render(request, 'index.html')

def register(request):
    print("11111111111111111111111111111111111111111111111111111")
    if request.method == "POST":
        try:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            address = request.POST['address']
            city = request.POST['city']
            postcode = request.POST['postcode']
            country = request.POST['country']
            state = request.POST['state']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']

            if password != confirmpassword:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'register.html')
            
            if User_Registration.objects.filter(email=email).exists():
                messages.error(request, 'User already registered.')
                return render(request, 'register.html')
            else:
                user = User_Registration.objects.create(
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    phonenumber=phonenumber,
                    address=address,
                    city=city,
                    postcode=postcode,
                    country=country,
                    state=state
                )
                user.set_password(password)  # Now we can use set_password
                user.save()
                messages.success(request, 'Registration successful!')
                return redirect('register.html')

        except Exception as e:
            print(f"Error: {e}")
            return render(request, 'register.html', {'message': 'An error occurred'})

    return render(request, 'register.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  

        if user is not None:
            auth_login(request, user)  
            return redirect("user-dashboard") 
        else:
            messages.error(request, 'Invalid email or password')
            
            
    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_dashboard(request):
    return render(request, 'user-dashboard.html',{'user': request.user})

@login_required
def checkout(request):
    return render(request, 'checkout.html')

@login_required
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

@login_required
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

def blog_detail_left_sidebar(request):
    return render(request , 'blog-detail-left-sidebar.html')

def elements_product(request):
    return render(request , 'elements-products.html')

def terms(request):
    return render(request , 'terms.html')

def forgot(request):
    return render(request , 'forgot.html')

def delete(request):
    return render(request,'cart.html')