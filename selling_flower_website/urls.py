"""selling_flower_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from products import views as products_views
from django.contrib.auth import views as auth_views
from django.conf.urls import handler404


# handler404 = '.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.home, name='home'),
    
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user-page.html', redirect_authenticated_user = True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('user/', include('users.urls')),
    path('add-to-cart/<int:pk>-quantity=<int:quantity>', users_views.add_to_cart, name='add-to-cart'),
    path('adjust-quantity/<int:pk>-quantity=<int:quantity>', users_views.adjust_quantity, name='adjust-quantity'),
    path('remove-single-item-from-cart/<int:pk>', users_views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('remove-item-from-cart/<int:pk>', users_views.remove_item_from_cart, name='remove-item-from-cart'),

    # For password reseting
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    path('products/', include('products.urls')),
    # path('cart/', include('cart.urls')),
    path('cart/', users_views.cart, name='cart'),
    # For facebook login
    path('accounts/', include('allauth.urls')),

    # For ckeditor, blog
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blogs/<int:pk>', products_views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/', products_views.BlogListView.as_view(), name='blog-list'),
    
    # Search box.
    path('search/', users_views.item_search_view, name='search'),
    path('auto-search/', users_views.auto_search, name='auto-search'),

    #call checkout 
    # path('proceed/',users_views.loadcheckout,name='checkout')
    # Test
    # path('test/',users_views.response_api,name='test')
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

if settings.DEBUG:
    # Thịnh's hint for uploading heroku.
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)