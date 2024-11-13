from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Use set_password to hash
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User_Registration(AbstractBaseUser, PermissionsMixin):

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phonenumber = models.PositiveBigIntegerField(default=0)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postcode = models.PositiveBigIntegerField(default=0)
    country = models.CharField(max_length=50, )  
    state = models.CharField(max_length=50, )
    
    is_active = models.BooleanField(default=True)  # Required for AbstractBaseUser
    is_staff = models.BooleanField(default=False)  # For admin access

    # Use email for login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    def set_password(self, raw_password):
        super().set_password(raw_password)
        
    def check_password(self, raw_password):
        return super().check_password(raw_password)    



# catgories and subcategories

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/')  

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='subcategories/')  

    def __str__(self):
        return self.name
    
    
class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='productsimg/')  

    def __str__(self):
        return f"Image for {self.product.name}"   

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    old_price = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)  
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0) 
    details=models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.name
