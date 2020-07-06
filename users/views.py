from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CheckoutForm, ProfileRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Order, ItemSelection
from products.models import Item, Blog, Category
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q, F
from topic.models import Topic
from django.http import JsonResponse
from django.views.generic import ListView
import random

# def handler404(request, *args, **argv):
#     return render(request, 'notfound-404.html', status=404)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        p_form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            new_user = User.objects.get(username=username)
            p_form.instance=new_user.profile # Indicating who this phone number belong to.
            if p_form.is_valid():
                p_form.save()
            else:
                print('invalid')
            messages.success(request, f'Your account {username} has been created. You can login now.')
            return redirect('login')
    
    else:
        form = UserRegisterForm()
        p_form = ProfileRegisterForm()
    return render(request, 'user-page-register.html', {'form': form, 'p_form': p_form})

def home(request):
    on_sale = Item.objects.filter(discount_percent__gte=0.01).order_by('-discount_percent')
    new_arrival = Item.objects.filter(tag__title = 'new')
    list_topic = Topic.objects.all()
    
    # Due to there is only 4 topic display in homepage, we will random them and get only four topics
    # Then we need to show only topics having at least 1 item
    topic_have_item = []
    for topic in Topic.objects.all():
        if topic.get_min_price_of_topic() != 0:
            topic_have_item.append(topic)
    list_topic_random_order = sorted(topic_have_item, key=lambda x: random.random())
    
    blogs = Blog.objects.all().order_by('-posted_date')[:3] # Get only 3 LASTEST blogs

    contexts = {
        'on_sale':on_sale,
        'new_arrival':  new_arrival,
        'list_topic': list_topic,
        'list_topic_random_order': list_topic_random_order,
        'blogs': blogs,
        }
    return render(request, 'index.html', contexts)

# For search button
def get_items_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        items = Item.objects.filter(
            Q(title__icontains=q) | 
            Q(tag__title__icontains=q) |
            Q(category__title__icontains=q)
        ).distinct()

        for item in items:
            queryset.append(item)
    return list(set(queryset))

def item_search_view(request):
    contexts = {}
    query = ""
    if request.method == 'GET':
        query = request.GET['q']
        contexts['query'] = str(query)
    
    items = get_items_queryset(query)

    if "order_by" in request.GET:
        kw_order_by = request.GET['order_by']
        if kw_order_by == 'asc-price':
            contexts['items'] = sorted(items,key=lambda x: x.price)
        elif kw_order_by == 'desc-price':
            contexts['items'] = sorted(items,key=lambda x: x.price, reverse=True)
        elif kw_order_by == 'by-name':  
            contexts['items'] = sorted(items,key=lambda x: x.title)
        elif kw_order_by == 'best-seller':
            contexts['items'] = sorted(items,key=lambda x: x.number_item_sold, reverse=True)
    else:
        contexts['items'] = items
    contexts['categories'] = sorted(Category.objects.all(), key=lambda x: random.random())
    contexts['type'] = '/search/'
    contexts['kwarg'] = query
    return render(request, 'product-list.html', contexts)
# End search button

# For autocomplete search
def auto_search(request):
    if 'term' in request.GET:
        q = request.GET.get('term')
        qs = Item.objects.filter(
            Q(title__icontains=q) | 
            Q(tag__title__icontains=q)| 
            Q(topic__title__icontains=q)
        ).distinct().values('id',value=F('title'))[:8]
        return JsonResponse(data=list(qs), safe=False) #Return json is required for jquery autocomplete
    return render(request, 'index.html')
# End autocomplete search

'''
NOTE: This lines of code for test purpose only 
from django.http import JsonResponse
def response_api(request):
    # temp = Item.objects.values('id','category','title', 'price', 'tag')
    on_sale = Item.objects.filter(discount_percent__gt=0.01).values('title', 'tag', 'discount_percent')
    # Data chỉ nhận mỗi kiểu: list bên trong nó là dict (hình như <=> json) ?
    return JsonResponse(
        data=list(on_sale),
        content_type='application/json', status=200, safe=False)
'''
'''
Sang's code
'''
def loadcheckout(request):
    return render (request,'checkout.html')

def get_user_pending_order(request):
    # get order for the correct user
    all_orders =  Order.objects.filter(user=request.user)
    proccessing_orders = all_orders.exclude(order_status='4').order_by('-date_ordered')
    if proccessing_orders.exists():
        # get the only order in the list of filtered orders
        return proccessing_orders
    return 0
    # return orders

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

    existing_orders = get_user_pending_order(request)
    print(existing_orders)
    contexts = {
        'u_form': u_form,
        'p_form': p_form,
        'orders': existing_orders
    }

    return render(request, 'account_order.html', contexts)
# Sang tạo 
def load_account_order(request):
    return render(request, 'account_order.html')

@login_required
def orders_detail(request):
    existing_orders = get_user_pending_order(request) 
    contexts ={
        'orders': existing_orders
    }
    print(existing_orders)
    return render(request, 'users/orders_detail.html', contexts)

@login_required
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order:
        if order.order_status == "1":
            order.order_status = "5"
            order.save()
            messages.success(request, f'Requested cancel order, waiting for acceptation.')
        else:
            messages.warning(request, f'Request failed. The order has been received and being proccessing.')
        return redirect('orders-detail')
        

@login_required
def checkout(request):
    checkout_items = ItemSelection.objects.filter(user=request.user, ordered=False, quantity__gt=0)
    
    if not checkout_items: #No item in cart -> Not allowed to checkout.
        messages.warning(request, f'You have no item to checkout.')
        return redirect('cart')

    '''
        NOTE: Check item stop bussiness and item don't have enough item just for logic insurance
        NOTE: Need to prevent user add to cart at the begin later.
    '''
    items_stop_selling = checkout_items.filter(item__stop_selling=True)
    if items_stop_selling:
        messages.warning(request, f'You are having stop bussiness item(s) in your cart. Please remove it then try again.')
        return redirect('cart')

    # Check number item available before checkout.
    failed_items = []
    for item in checkout_items:
        number_left = item.item.number_item_left - item.quantity
        if number_left < 0:
            failed_items.append(item)
    if failed_items:
        messages.warning(request, f'Checkout failed. We do not have enough '+ ", ".join([i.item.title for i in failed_items]) + ' by now.')
        return redirect('cart')

    total_cost = sum(i.get_final_price() for i in checkout_items)
    
    if request.method == 'GET':
        # Check if client edit the order info.
        if 'receiver' in request.GET or 'address' in request.GET or 'phone' in request.GET:
            checkout_form = CheckoutForm(initial={
                'receiver': request.GET.get('receiver'),
                'phone': request.GET.get('phone'),
                'address': request.GET.get('address')
                }
            )
        else: #Just render the checkout page.
            checkout_form = CheckoutForm(initial={
                'receiver': request.user.last_name + " " + request.user.first_name,
                'phone': request.user.profile.phone,
                'address': request.user.profile.address
                }
            )
        contexts={
            'checkout_items': checkout_items,
            'total_cost': total_cost,
            'checkout_form': checkout_form
        }
        
        # return render(request, 'users/checkout.html', contexts)
        return render(request, 'checkout.html', contexts)
    else: #This is POST method
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            receiver = checkout_form.cleaned_data['receiver']
            phone = checkout_form.cleaned_data['phone']
            address = checkout_form.cleaned_data['address']

            new_order = Order.objects.create(
                user=request.user,
                receiver=receiver,
                phone=phone,
                address=address
            )

            for item in checkout_items:
                new_order.items_ordered.add(item)
                # Decreasing number of item left NO NEED TO CHECK NUMBER IS VALID HERE, CHECKED ABOVE.
                item.item.number_item_left -= item.quantity
                item.item.number_item_sold += item.quantity
                item.item.save()
                # Change ItemSelection 'ordered' to True 
                item.ordered=True
                # This item's price won't be change after client bought it.
                # This price is the final price, discounted.
                item.price_client_bought = item.item.get_final_price()
                item.save()

            messages.success(request, f'Checkout successfully. Your order will be delivery soon.')
            return redirect('cart')
        else:
            messages.warning(request, f'Checkout failed. Check your info and try again.')
            return redirect('checkout')

@login_required
def cart(request):
    selected_items = ItemSelection.objects.filter(user=request.user,ordered=False)
    total_cost = sum(i.get_final_price() for i in selected_items)
    old_cost = sum(i.get_total_item_price() for i in selected_items)
    contexts={
            'selected_items':selected_items,
            'total_cost': total_cost,
            'old_cost': old_cost,
    }
    return render(request, 'cart.html', contexts)


'''
ItemSelection sẽ là item trong cart, có user có trạng thái ordered và trỏ tới item
Khi checkout, ItemSelection sẽ có ordered = True, lúc này tạo order mới.
'''
@login_required
def add_to_cart(request, pk, quantity):
    if quantity == 0:
        messages.warning(request, f'Unavailable quantity.')
        return redirect('item-detail', pk)
    # Get the id of item
    item = get_object_or_404(Item, pk=pk)

    # Check quantity is bigger than number_item_left?
    if quantity > item.number_item_left:
        messages.warning(request, f"Sorry. We just have "+ str(item.number_item_left) + " item(s) of " +item.title+" by now.")
        return redirect('item-detail', pk)
    # Create a new ItemSelection if adding item is not exist in cart.
    selected_item, created = ItemSelection.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    # If not created new item selection -> exist selected item, selected item quantity += quantity.
    if not created:  #If get_or_create() not created a new ItemSelection
        # Total quantity of a item in cart must less than that item's number_item_left.
        if selected_item.quantity + quantity > item.number_item_left: 
            messages.warning(request, f"Sorry. We just have "+ str(item.number_item_left) + " item(s) of " +item.title+" by now.")
            return redirect('item-detail', pk)
        selected_item.quantity += quantity
        selected_item.save()
    else: # If created a new itemselection -> there is no similar item in cart -> create and assign quantity 
        selected_item.quantity = quantity
        selected_item.save()
    messages.info(request, "This item was added to your cart.")
    return redirect('item-detail', pk)


@login_required
def adjust_quantity(request, pk, quantity):
    item = get_object_or_404(Item, pk=pk) #Get item adjusting quantity for checking available item

    # Need to check quantity = 0 -> Delete item from cart?
    if quantity > item.number_item_left:
        messages.warning(request, f"Sorry. We don't have enough " +item.title+"by now.")
        return redirect('item-detail', pk)
    # Create a new ItemSelection if adding item is not exist in cart.
    selected_item, created = ItemSelection.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    selected_item.quantity = quantity
    selected_item.save()
    messages.info(request, "{}'s quantity was updated.".format(selected_item.item.title))
    return redirect('cart')

@login_required
def remove_item_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    try: #Case: Having this item in cart
        selected_item = ItemSelection.objects.get(
                item=item,
                user=request.user,
                ordered=False
        )
        selected_item.delete()
        messages.info(request, "This item quantity was updated.")
    except: #Case: Not have this item in cart
        messages.info(request, "This item was not in your cart")
    return redirect('cart')

@login_required
def remove_single_item_from_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    try: #Case: Having this item in cart
        selected_item = ItemSelection.objects.get(
                item=item,
                user=request.user,
                ordered=False
        )
        if selected_item.quantity > 1:
            selected_item.quantity -= 1
            selected_item.save()
        else:
            selected_item.delete()
        messages.info(request, "This item quantity was updated.")
    except: #Case: Not have this item in cart
        messages.info(request, "This item was not in your cart")
    return redirect('item-detail', pk)
