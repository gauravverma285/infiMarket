from django.urls import path
from .api import*

urlpatterns = [
    path('category/',CategoryAPIViews.as_view(),name="category"),
    path('product/',ProductAPIViews.as_view(),name="category"),

]