from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Order, ItemSelection
from products.models import Item
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

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
    orders = Order.objects.filter(customer_info=user_profile, ordered=True)
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

@login_required
def cart(request):
    try:
        '''
        This func is only able to get one order till now.
        Need to find out if an user can have more than an order which "ordered=False"?
        '''
        orders = Order.objects.get(customer_info__user=request.user,ordered=False)
        print(orders)
    except:
        return render(request, 'users/cartt.html')
    return render(request, 'users/cartt.html', {'orders':orders})


@login_required
def add_to_cart(request, pk):
    # Get the id of item
    item = get_object_or_404(Item, pk=pk)
    # user_profile = get_object_or_404(Profile, user=request.user)
    # Create a new ItemSelection if adding item is not exist in cart.
    selected_item, created = ItemSelection.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    # Check if there is any order of user requesting.
    order_qs = Order.objects.filter(
        customer_info__user=request.user,
        ordered=False
    ) # <=> order query set
    if order_qs.exists(): # There is order
        order = order_qs[0] # Get the exactly order of the user.
        # check if the order item is in the order
        if order.items_ordered.filter(item__pk=item.pk).exists():
            selected_item.quantity += 1
            selected_item.save()
            # messages.info(request, "This item quantity was updated.")
            # This should redirect to summary checkout.
            return redirect('item-detail', pk)
            # return redirect("core:order-summary")
        else:
            order.items_ordered.add(selected_item)
            messages.info(request, "This item was added to your cart.")
            # return redirect("core:order-summary")
            return redirect('item-detail', pk)
    else:
        order = Order.objects.create(
            customer_info=request.user.profile)
        order.items_ordered.add(selected_item)
        messages.info(request, "This item was added to your cart.")
        # return redirect("core:order-summary")
        return redirect('item-detail', pk)


@login_required
def remove_item_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_qs = Order.objects.filter(
        customer_info__user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items_ordered.filter(item__pk=item.pk).exists():
            order_item = ItemSelection.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items_ordered.remove(order_item)
            
            order_item.delete()
            messages.info(request, "This item was removed.")
            return redirect('cart')
            # return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('cart')
            # return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        # return redirect("core:product", slug=slug)
        return redirect('cart')

@login_required
def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    order_qs = Order.objects.filter(
        customer_info__user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items_ordered.filter(item__pk=item.pk).exists():
            order_item = ItemSelection.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items_ordered.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect('item-detail', pk)
            # return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('item-detail', pk)
            # return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        # return redirect("core:product", slug=slug)
        return redirect('item-detail', pk)
