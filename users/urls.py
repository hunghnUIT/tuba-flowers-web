from django.urls import path
from . import views

urlpatterns = [
    path('orders_detail', views.orders_detail, name="orders_detail"),
    path('profile', views.profile, name="profile"),
    path('cart/', views.cart, name='cart'),
    path('cart/checkout', views.checkout, name='checkout'),
    
]