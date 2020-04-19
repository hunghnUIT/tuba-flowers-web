from django.urls import path
from .views import ItemsWithCategoryListView, ItemDetailView
from . import views

urlpatterns = [
    path('', views.allItems, name = 'products-all'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name = 'item-detail'),
    path('category/<str:category>', ItemsWithCategoryListView.as_view(), name = 'products-category'),
]