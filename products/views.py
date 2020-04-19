from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.views.generic import ListView, DetailView

def allItems(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'products/all_items.html', context)

class ItemsWithCategoryListView(ListView): # Click at an category and it return items with the same category.
    model = Item
    template_name = 'products/items_category.html' # Format of the file's name: <app>/<model>_<viewtype>.html
    context_object_name = 'items'
    paginate_by = 12
    # ordering = ['-price'] or ['price'] depended on the order user's choice.

    def get_queryset(self): # Get the list of items for this view.
        cate = self.kwargs.get('category')
        return Item.objects.filter(category = cate)

class ItemDetailView(DetailView):
    model = Item

    # By default, the generic class-based will looking for template <app>/<model>_<viewtype>.html
    # So it's unnecessary to have the line "template_name = 'products/item_detail.html'"
    # as long as we created a file exactly is item_detail.html in templates/products folder


