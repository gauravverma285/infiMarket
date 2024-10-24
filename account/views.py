from django.shortcuts import render
from .models import User_Registration
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
import random
# Create your views here.



def index(request):
    return render(request, 'index.html')

def register(request):
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
            # print(f"Error: {e}")
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
    if request.method == 'POST':
        email = request.POST.get('email', '').strip() 
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            if user:
                otp = random.randint(1000, 9999)  
                request.session['otp'] = otp
                request.session['email'] = email
              
                send_mail(
                    'Password Reset OTP',
                    f'Your OTP for password reset is {otp}.',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return redirect('otp')  
        except User.DoesNotExist:
            messages.error(request, 'Email does not exist.')
    return render(request , 'forgot.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def otp(request):
    if request.method == 'POST':
        otp_input = request.POST.get('otp_full')  
        session_otp = request.session.get('otp')

        if otp_input is None:
            messages.error(request, 'OTP input is required.')
            return render(request, 'otp.html')

        if session_otp is None:
            messages.error(request, 'Session has expired or OTP is not set.') 
            return render(request, 'otp.html')

        try:
            otp_input_int = int(otp_input) 
            session_otp_int = int(session_otp)     
            if otp_input_int == session_otp_int:
                return redirect('newpassword')  
            else:
                messages.error(request, 'Invalid OTP.')
        except ValueError as e:
            print(e)
            messages.error(request, 'OTP must be a number.')

    return render(request, 'otp.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def new_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirmnewpassword')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'newpassword.html')

        try:
            session_email = request.session.get('email')  
            if not session_email:
                messages.error(request, 'Session expired or invalid session. Please try again.')
                return redirect('login') 
            User = get_user_model()
            user = User.objects.get(email=session_email)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('login')  
        except user.DoesNotExist:
            messages.error(request, 'user not found')    
            return render(request, 'forget.html')
    else:
        return render(request, 'newpassword.html')
    
def delete(request):
    return render(request,'cart.html')