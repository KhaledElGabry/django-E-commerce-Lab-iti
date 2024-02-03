from django.contrib import admin
from django.urls import path, include 
from . import views


urlpatterns = [
    path('', views.home, name='home'),    
    path('home/', views.home, name='home'),    
    path('product/', views.product, name='product'),    
    path('productDetail/<int:productID>/', views.productDetail, name='productDetail'),
    path('about/', views.about, name='about'),
    path('category/', views.category, name='category'),
]