from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Order

def register(request):
    if request.method == 'POST':
        print('POST')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            print(form.cleaned_data)

            messages.success(request, f'Your account {username} has been created. You can login now.')
            return redirect('home')
    
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    if request.method == 'POST': # Check if we trying to POST data, which means we are trying to save data.
        # So we will save what we have just entered to forms.
        # We add request.POST to pass in the post data (Truyền đi dữ liệu mới nhập)
        # It's necessary to add request.POST unless the data won't be updated in the box data BUT IT'S NOT BEEN SAVED YET.
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # Now we check the forms validation and if they are, save them.
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account profile has been updated!')
            return redirect('profile')

    else: # This case we are trying to get the page only.
        # Give argument "instance" to give current user info to those forms
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    contexts = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', contexts)

def get_user_pending_order(request):
    # get order for the correct user
    user_profile = get_object_or_404(Profile, user=request.user)
    orders = Order.objects.filter(customer_info=user_profile, status=False)
    if orders.exists():
        # get the only order in the list of filtered orders
        return orders
    return 0
    # return orders

@login_required
def orders_detail(request):
    existing_orders = get_user_pending_order(request) 
    contexts ={
        'orders': existing_orders
    }
    print(existing_orders)
    return render(request, 'users/orders_detail.html', contexts)
