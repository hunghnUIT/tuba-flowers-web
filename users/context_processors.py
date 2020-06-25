from users.models import ItemSelection
def add_variable_to_context(request):
    number_item_in_cart = 0
    if request.user.is_authenticated:
        number_item_in_cart = sum([item.quantity for item in ItemSelection.objects.filter(user=request.user,ordered=False)])
    return {
        'number_item_in_cart': number_item_in_cart
    }
    