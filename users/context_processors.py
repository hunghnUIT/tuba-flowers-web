from users.models import ItemSelection
from topic.models import Topic

def add_variable_to_context(request):
    number_item_in_cart = 0
    if request.user.is_authenticated:
        number_item_in_cart = sum([item.quantity for item in ItemSelection.objects.filter(user=request.user,ordered=False)])
    
    list_topic = Topic.objects.all()
    
    return {
        'number_item_in_cart': number_item_in_cart,
        'list_topic': list_topic
    }
    