from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.views.generic import ListView, DetailView
# from products.models import Property

class ItemsListView(ListView):
    model = Item
    template_name = 'product-list.html' # Format of the file's name: <app>/<model>_<viewtype>.html
    # template_name= 'products/all_items.html'
    context_object_name = 'items'
    paginate_by = 12

    # Custom a order_by sort by final price.
    # qs = Item.objects.all()
    # qs = sorted(qs, key: lambda i: i.roll_numb().split('-')[1]) #Not edit yet
    
    def get_queryset(self): # Get the list of items for this view.
        # queryset = super(ItemsListView, self).get_queryset()
        kw_order_by = self.request.GET.get('order_by')
        available_items = Item.objects.filter(stop_selling=False) #Show only items on selling.
        if kw_order_by:
            if kw_order_by == 'asc-price':
                return available_items.order_by('price')
            if kw_order_by == 'desc-price':
                return available_items.order_by('-price')
            if kw_order_by == 'by-name':
                return available_items.order_by('title')
            if kw_order_by == 'best-seller':
                return available_items.order_by('-number_item_sold')
        else:
            return available_items

class ItemsWithCategoryListView(ListView): # Click at an category and it return items with the same category.
    model = Item
    template_name = 'product-list.html' # Format of the file's name: <app>/<model>_<viewtype>.html
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self): # Get the list of items for this view.
        kw_order_by = self.request.GET.get('order_by')
        cate = self.kwargs.get('category')
        items_match = Item.objects.filter(category__contains = cate)
        available_items = items_match.filter(stop_selling=False)
        if kw_order_by:
            if kw_order_by == 'asc-price':
                return available_items.order_by('price')
            if kw_order_by == 'desc-price':
                return available_items.order_by('-price')
            if kw_order_by == 'by-name':
                return available_items.order_by('title')
            if kw_order_by == 'best-seller':
                return available_items.order_by('-number_item_sold')
        
        return available_items

class ItemsWithTopicListView(ListView): # Choose a topic and it return items with the same topic.
    model = Item
    template_name = 'product-list.html' # Format of the file's name: <app>/<model>_<viewtype>.html
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self): # Get the list of items for this view.
        kw_order_by = self.request.GET.get('order_by')
        topic = self.kwargs.get('topic')
        items_match = Item.objects.filter(topic = topic[0].capitalize())
        available_items = items_match.filter(stop_selling=False)
        if kw_order_by:
            if kw_order_by == 'asc-price':
                return available_items.order_by('price')
            if kw_order_by == 'desc-price':
                return available_items.order_by('-price')
            if kw_order_by == 'by-name':
                return available_items.order_by('title')
            if kw_order_by == 'best-seller':
                return available_items.order_by('-number_item_sold')
        
        return available_items

class ItemsWithTagListView(ListView): # Choose a tag and it return items containing that tag.
    model = Item
    template_name = 'product-list.html' # Format of the file's name: <app>/<model>_<viewtype>.html
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self): # Get the list of items for this view.
        kw_order_by = self.request.GET.get('order_by')
        tag = self.kwargs.get('tag')
        items_match = Item.objects.filter(tag__contains = tag)
        available_items = items_match.filter(stop_selling=False)
        if kw_order_by:
            if kw_order_by == 'asc-price':
                return available_items.order_by('price')
            if kw_order_by == 'desc-price':
                return available_items.order_by('-price')
            if kw_order_by == 'by-name':
                return available_items.order_by('title')
            if kw_order_by == 'best-seller':
                return available_items.order_by('-number_item_sold')
        
        return available_items

class ItemDetailView(DetailView):
    model = Item

    template_name = 'product-detail.html'
    # By default, the generic class-based will looking for template <app>/<model>_<viewtype>.html
    # So it's unnecessary to have the line "template_name = 'products/item_detail.html'"
    # as long as we created a file exactly is item_detail.html in templates/products folder


