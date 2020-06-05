from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from django.urls import reverse_lazy

urlpatterns = [
    path('orders_detail', views.orders_detail, name="orders_detail"),
    path('profile', views.profile, name="profile"),
    # path('cart/', views.cart, name='cart'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('password-change', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url=reverse_lazy('password-change-done')
    ), name='password-change'),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password-change-done'),
    
]